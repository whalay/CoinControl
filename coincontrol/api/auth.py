from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource
from .decorators import monitor
from flask import Blueprint, request
from coincontrol.forms import RegistrationForm
from coincontrol.models import Users
from coincontrol.extensions import db

api_auth = Blueprint("api_auth", __name__)
api = Api(api_auth, prefix="/api/v1")


auth = HTTPBasicAuth()


class Register(Resource):
   
    @monitor
    def post(self):
        # app login written here
        user_data = request.get_json()
        username = user_data["username"]
        email = user_data["email"]
        password = user_data["password"]
        confirm_password = user_data["confirm_password"]

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
            db.session.add(user)
            db.session.commit()

            response = {
                "status": 201,
                "message": "User created sucessfully",
                "metadata": {"username": username, "email": email},
            }
            
            return response, 201
        else:
            
            response = {
                "status": 400,
                "message": "User not created",
                "error": form.errors
            }

            return response, 400


api.add_resource(Register, "/register")


class Login(Resource):
    response = {"status": 400}

    @monitor
    def post(self):
        # app login written here
        
        pass


api.add_resource(Login, "/login")


class LoginOut(Resource):
    response = {"status": 400}

    @monitor
    def post(self):
        # app login written here
        pass


api.add_resource(LoginOut, "/logout")
