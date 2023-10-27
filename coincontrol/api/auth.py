from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource
from .decorators import monitor
from flask import Blueprint, request
from flask_jwt_extended import create_access_token, create_refresh_token , jwt_required, get_jwt, get_jwt_identity
from coincontrol.forms import RegistrationForm, LoginForm
from coincontrol.models import Users
from coincontrol.extensions import db, bcrypt
from coincontrol.api.blacklist import BLACKLIST
from http import HTTPStatus


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
                form.username.data = username
                form.email.data = email
                form.password.data = password
                form.confirm_password.data = confirm_password

                username = form.username.data
                email = form.email.data
                password = form.password.data
                confirm_password = form.confirm_password.data

                user = Users(username=username, email=email, password=password)
                user.generate_password_hash(password)
                access_token = create_access_token(identity=)
                db.session.add(user)
                db.session.commit()

                response = {
                    "status": 201,
                    "message": "User created sucessfully",
                    "data": {
                        "status": "success",
                        "username": username, 
                        "email": email
                    }
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
                "data": {
                "status": "failed",
                "error": str(e)
                },
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
                        "data": {
                            "status": "failed",
                            "error": "Invalid credentials"
                        }
                    }
                    return response, 404

                if not bcrypt.check_password_hash(user.password, password):
                    response = {
                        "status": 401,
                        "message": "Invalid password for this account, password might be case sensitive",
                        "data": {
                            "status": "failed",
                            "error": "Invalid credentials"
                        },
                    }
                    return response, 401
                
                access_token = create_access_token(identity=email)
                refresh_token = create_refresh_token(identity=email)

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
                
            
                return response, 200

        except Exception as e:
            response = {
            "status": 500,
            "message": "Internal server error",
                "data": {
                "status": "failed",
                "error": str(e)
                },
            }
            
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
       
        return response, 200


api.add_resource(LoginOut, "/logout")

class RefreshToken(Resource):
    
    @jwt_required(refresh=True)
    @monitor
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        response = {
            "status": 200,
            "message": "Access token created successfully",
            "data": {
                "status": "success",
                "access_token": access_token
            },
        }
        return response, 200
        
api.add_resource(RefreshToken, "/refresh")