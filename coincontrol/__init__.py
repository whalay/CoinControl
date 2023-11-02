from datetime import timedelta

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_cors import CORS
from flask_login import LoginManager, current_user
from flask_wtf import CSRFProtect

from coincontrol.api.admin import api_admin_bp
from coincontrol.api.auth import api_auth_bp
from coincontrol.api.blacklist import BLACKLIST
from coincontrol.api.user import api_user_bp
from coincontrol.auth import auth_bp
from coincontrol.config import config
from coincontrol.extensions import db, jwt, migrate
from coincontrol.models import Users
from coincontrol.user import main_bp


def create_app(config_name="development"):
    app = Flask(__name__)

    # setting up configuration from the development object
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # register blueprints here
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_auth_bp)
    app.register_blueprint(api_user_bp)
    app.register_blueprint(api_admin_bp)

    # initialize csrf for flask forms
    CSRFProtect(app)

    # configure Cors
    CORS(app)

    # initialize flask migrate
    migrate.init_app(app, db)

    # initialize jwt
    jwt.init_app(app)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=1)
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=15)
    app.config["REMEMBER_COOKIE_DURATION"] = timedelta(hours=1)
    app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_SESSION_COOKIE"] = timedelta(hours=1)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.user_id

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return Users.query.filter_by(user_id=identity).one_or_none()

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLACKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        response = {
            "status": 401,
            "message": "User has been logged out",
            "data": {
                "error": "token_revoked",
            },
        }
        return response, 401

    @jwt.invalid_token_loader
    def invalid_token_callback(invalid_token):
        response = {
            "status": 422,
            "message": "Invalid token",
            "data": {
                "error": "This token is invalid",
            },
        }
        return response, 422

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        response = {
            "status": 400,
            "message": "Expired token",
            "data": {
                "error": "This token has expired",
            },
        }
        return response, 400

    # flask login manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    # login_manager.login_message ='Opps only admin users are authorized to access this page'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        user = Users.query.get(user_id)

        if user:
            return user
        else:
            return None

    @login_manager.unauthorized_handler
    def unauthorized_user():
        if current_user.is_authenticated:
            return render_template("dashboard/dashboard.html")
        else:
            if request.endpoint == "auth.admin":
                flash("Opps only admin users are authorized to access this page")
            else:
                flash("Please log in to access this page.")
            return redirect(url_for("auth.login"))

    # initialize the db
    db.init_app(app)

    return app
