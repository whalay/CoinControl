import unittest
from coincontrol.extensions import db
from coincontrol.models import Users
from coincontrol import create_app

"""
Code Analysis

Main functionalities:
The Register class is a Flask RESTful resource that handles user registration. It receives user data in JSON format, validates it using the RegistrationForm class, creates a new user in the Users table of the database, and returns a response with a status code and a message.

Methods:
- post: receives user data, validates it using RegistrationForm, creates a new user in the database, and returns a response with a status code and a message.

Fields:
- None.
"""


class TestRegister(unittest.TestCase):
    def create_app(self):
        # Creating a test flask application
        # It takes in a parameter called testing which is passed as an argument to the config_name variable
        app = create_app(config_name="testing")
        return app

    def setUp(self):
        # Creating and configuring the test database
        self.app = self.create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        # Cleaning up the test database
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # Tests that a user can register with valid data
    def test_valid_user_registration(self):
        username = "testuser"
        email = "testuser@test.com"
        password = "Test1234@"
        confirm_password = "Test1234@"

        data = {
            "username": username,
            "email": email,
            "password": password,
            "confirm_password": confirm_password,
        }

        tester = self.client
        response = tester.post("/api/v1/register", json=data)

        r = {
            "status": 201,
            "message": "User created sucessfully",
            "data": {
                "status": "success",
                "username": username, 
                "email": email
            }
        }

        # Verify the response status code and the returned JSON data
        self.assertEqual(response.status_code, 201)
        self.assertEqual(r, response.json)

    # Tests that a user can register with valid data and special characters in password
    def test_user_registration_with_special_characters_in_password(self):
        username = "testuser"
        email = "testuser@test.com"
        password = "Test1234@#"
        confirm_password = "Test1234@#"

        data = {
            "username": username,
            "email": email,
            "password": password,
            "confirm_password": confirm_password,
        }

        tester = self.client
        response = tester.post("/api/v1/register", json=data)

        r = {
            "status": 201,
            "message": "User created sucessfully",
            "data": {
                "status": "success",
                "username": username, 
                "email": email
            }
        }

        # Verify the response status code and the returned JSON data
        self.assertEqual(response.status_code, 201)
        self.assertEqual(r, response.json)

    # Tests that a user cannot register without a username
    def test_user_registration_with_missing_username(self):
        username = " "
        email = "testuser@test.com"
        password = "Test1234@#A"
        confirm_password = "Test1234@#A"

        data = {
            "username": username,
            "email": email,
            "password": password,
            "confirm_password": confirm_password,
        }

        tester = self.client
        response = tester.post("/api/v1/register", json=data)
       
        r = {
            "status": 400,
            "message": "User not created",
            "data": {
                "status":"failed",
                "error": {"username": ["This field is required."]}
            }
        }

        # Verify the response status code and the returned JSON data
        self.assertEqual(response.status_code, 400)
        self.assertEqual(r, response.json)

    # Tests that a user cannot register without an email
    def test_user_registration_with_missing_email(self):
        username = "testuser"
        email = ""
        password = "Test1234@#A"
        confirm_password = "Test1234@#A"

        data = {
            "username": username,
            "email": email,
            "password": password,
            "confirm_password": confirm_password,
        }

        tester = self.client
        response = tester.post("/api/v1/register", json=data)
        
        r = {
            "status": 400,
            "message": "User not created",
            "data": {
                "status":"failed",
                "error": {"email": ["This field is required."]}
            }
        }

        # Verify the response status code and the returned JSON data
        self.assertEqual(response.status_code, 400)
        self.assertEqual(r, response.json)

