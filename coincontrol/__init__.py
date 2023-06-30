from flask import Flask
from flask_wtf import CSRFProtect 
from flask_jwt_extended import JWTManager
from coincontrol.config import config
from coincontrol.auth import auth
from coincontrol.main import main
from coincontrol.extensions import db
from coincontrol.api.auth import api_auth
from coincontrol.api.main import api_main
from coincontrol.auth import auth
from coincontrol.main import main
from datetime import timedelta


def create_app(config_name='development'):
    app = Flask(__name__)
    
    # setting up configuration from the development object
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
   
    # register blueprints here
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(api_auth)
    app.register_blueprint(api_main)
    
    # initialize csrf for flask forms
    CSRFProtect(app)
    app.config['WTF_CSRF_ENABLED'] = False
   
    # initialize jwt
    jwt = JWTManager(app)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=1)
    
    from coincontrol.api.blacklist import BLACKLIST
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
        return response
    
    # initialize the db 
    db.init_app(app)
    
    return app

