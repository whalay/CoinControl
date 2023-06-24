from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource
from .decorators import monitor


# auth = HTTPBasicAuth()

class Register(Resource):
    response = {"status":400,"message":"User not created"}
    
    @monitor
    def post(self):
        # app login written here
        
        
        self.response["status"] = 201
        self.response["message"] = "User created sucessfully"
        return self.response, 201
        

class Login(Resource):
    response = {"status":400}
    
    @monitor
    def post(self):
        # app login written here
        pass

class LoginOut(Resource):
    response = {"status":400}
    
    @monitor
    def post(self):
        # app login written here
        pass