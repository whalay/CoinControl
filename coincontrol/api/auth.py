from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    current_user,
    get_jwt,
    jwt_required,
    set_access_cookies,
    unset_jwt_cookies,
)
from flask_restful import Api, Resource

from coincontrol.api.blacklist import BLACKLIST
from coincontrol.extensions import bcrypt, db
from coincontrol.forms import LoginForm, RegistrationForm
from coincontrol.helpers import set_cookie
from coincontrol.models import Users

from .decorators import monitor

api_auth_bp = Blueprint("api_auth_bp", __name__)
api = Api(api_auth_bp, prefix="/api/v1")


class Register(Resource):
    @monitor
    def post(self):
        # app login written here
        try:
            user_data = request.get_json()
            username = user_data.get("username")
            email = user_data.get("email")
            password = user_data.get("password")
            confirm_password = user_data.get("confirm_password")

            form = RegistrationForm()

            if form.validate():
                username, email, password, confirm_password = (
                    form.username.data,
                    form.email.data,
                    form.password.data,
                    form.confirm_password.data,
                )

                if username and email and password and confirm_password:
                    user = Users(username=username, email=email, password=password)
                    user.generate_password_hash(password)
                    db.session.add(user)
                    db.session.commit()
                    response = {
                        "status": 201,
                        "message": "User created sucessfully",
                        "data": {
                            "status": "success",
                            "username": username,
                            "email": email,
                        },
                    }
                    return response, 201
            else:
                response = {
                    "status": 400,
                    "message": "User not created",
                    "data": {
                        "status": "failed",
                        "error": form.errors,
                    },
                }

                return response, 400

        except Exception as e:
            response = {
                "status": 500,
                "message": "Internal server error",
                "data": {"status": "failed", "error": str(e)},
            }

            return response, 500


api.add_resource(Register, "/register")


class Login(Resource):
    @monitor
    def post(self):
        # app login written here
        try:
            user_data = request.get_json()
            email = user_data.get("email")
            password = user_data.get("password")

            form = LoginForm()

            if form.validate():
                form.email.data = email
                form.password.data = password

                email = form.email.data
                password = form.password.data

                user = Users.query.filter_by(email=email).first()

                if not user:
                    response = {
                        "status": 404,
                        "message": "This user does not exist",
                        "data": {"status": "failed", "error": "Invalid credentials"},
                    }
                    return response, 404

                if not bcrypt.check_password_hash(user.password, password):
                    response = {
                        "status": 401,
                        "message": "Invalid password for this account, password might be case sensitive",
                        "data": {"status": "failed", "error": "Invalid credentials"},
                    }
                    return response, 401

                access_token = create_access_token(identity=user, fresh=True)
                refresh_token = create_refresh_token(identity=user)

                response = {
                    "status": 200,
                    "message": "Logged in successfully",
                    "data": {
                        "status": "success",
                        "username": user.username,
                        "email": user.email,
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    },
                }
                # response = make_response(response)
                # response = set_cookie(response, access_token)
                return response, 200

        except Exception as e:
            response = {
                "status": 500,
                "message": "Internal server error",
                "data": {"status": "failed", "error": str(e)},
            }
            print(e)
            return response, 500


api.add_resource(Login, "/login")


class LoginOut(Resource):
    @jwt_required()
    @monitor
    def post(self):
        # app login written here
        jwt_token = get_jwt()["jti"]
        BLACKLIST.add(jwt_token)
        response = {
            "status": 200,
            "message": "You have been logged Out successfully",
        }
        # unset_jwt_cookies(response)
        return response, 200


api.add_resource(LoginOut, "/logout")


class RefreshToken(Resource):
    @jwt_required(refresh=True)
    @monitor
    def post(self):
        access_token = create_access_token(identity=current_user, fresh=True)
        response = {
            "status": 200,
            "message": "Access token created successfully",
            "data": {
                "status": "success",
                "access_token": access_token,
                "id": current_user.user_id,
                "username": current_user.username,
                "email": current_user.email,
            },
        }
        return response, 200

api.add_resource(RefreshToken, "/refresh")


# Account management
class UserProfile(Resource):
    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        try:
            user = Users.query.filter_by(user_id=current_user.user_id).first()
            if user is not None:
                response = {
                    "status": 200,
                    "message": "User profile fetched successfully",
                    "data": {
                        "status": "success",
                        "alternative_id": user.alternative_id,
                        "name": user.username,
                        "email": user.email,
                        "verified": user.verified,
                        "is_active": current_user.is_active,
                        "is_admin": user.is_admin,
                    },
                }
                return response, 200
            else:
                response = {
                    "status": 404,
                    "message": "User not found",
                    "data": {
                        "status": "failed",
                    },
                }
                return response, 404
        except Exception as e:
            print(e)

    @monitor
    @jwt_required(fresh=True)
    def put(self):
        # app logic written here
        try:
            user_data = request.get_json()
            username = user_data.get("username", "")
            email = user_data.get("email", "")
            password = user_data.get("password", "")
            confirm_password = user_data.get("confirm_password", "")
            user = Users.query.filter_by(user_id=current_user.user_id).first()
            form = RegistrationForm()
            if form.validate():
                username, email, password, confirm_password = (
                    form.username.data,
                    form.email.data,
                    form.password.data,
                    form.confirm_password.data,
                )
                if username and email and password and confirm_password:
                    user.username, user.email = username, email
                    user.generate_password_hash(password)
                    db.session.commit()
                    response = {
                        "status": 200,
                        "message": "User profile updated successfully",
                        "data": {
                            "status": "success",
                            "username": user.username,
                            "email": user.email,
                        },
                    }
                    return response, 200
            else:
                response = {
                    "status": 400,
                    "message": "Profile Update failed",
                    "data": {
                        "status": "failed",
                        "error": form.errors,
                    },
                }
                return response, 400
        except Exception as e:
            print(e)


api.add_resource(UserProfile, "/user/profile")
