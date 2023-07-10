import unittest
from coincontrol.extensions import db
from coincontrol.models import Users
from coincontrol import create_app
# from unittest.mock import patch

"""
Code Analysis

Main functionalities:
The Register class is responsible for handling user registration. It receives user data in JSON format, validates it using the RegistrationForm class, creates a new user in the Users table of the database, and returns a response with a status code and a message.

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


"""
Code Analysis

Main functionalities:
The Login class is responsible for handling user login requests. It receives user data in JSON format, checks if the email exists in the database, and verifies the password. If the credentials are correct, it generates access and refresh tokens using the Flask-JWT-Extended extension and returns them in the response.

Methods:
- post: receives the user data in JSON format, checks the credentials, generates access and refresh tokens, and returns them in the response.

Fields:
- No relevant fields in the Login class. However, the Users class defines the fields for the user model, such as user_id, username, password, email, verified, is_admin, date_created, and date_verified.
"""
class TestLogin(unittest.TestCase):
    def create_app(self):
        app = create_app(config_name="testing")
        return app

    def setUp(self):
        self.app = self.create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    # Tests that a valid email and password returns access and refresh tokens
    def test_valid_login_returns_tokens(self):
        username = 'test'
        email = 'test@test.com'
        password = 'Test2@'

        user = Users(username=username, email=email, password=password)
        user.generate_password_hash(password)
        db.session.add(user)
        db.session.commit()

        tester = self.client
        response = tester.post("/api/v1/login", json={'email': email, 'password': password})
        res = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', res['data'])
        self.assertIn('refresh_token', res['data'])

    # Tests that a valid email and password returns status code 200
    def test_valid_login_returns_status_code_200(self):
        username = 'test'
        email = 'test@test.com'
        password = 'Test2@'

        user = Users(username=username, email=email, password=password)
        user.generate_password_hash(password)
        db.session.add(user)
        db.session.commit()
        
        tester = self.client
        response = tester.post("/api/v1/login", json={'email': email, 'password': password})
        self.assertEqual(response.status_code, 200)
        
    
    # Tests that an invalid email returns status code 400
    def test_invalid_email(self):
        username = 'test'
        email = 'test@test.com'
        password = 'Test2@'

        user = Users(username=username, email=email, password=password)
        user.generate_password_hash(password)
        db.session.add(user)
        db.session.commit()
        
        tester = self.client
        response = tester.post("/api/v1/login", json={'email': 'test1@test.com', 'password': password})
        self.assertEqual(response.status_code, 404)

      # Tests that an invalid password returns status code 401
    def test_invalid_password(self):
        username = 'test'
        email = 'test@test.com'
        password = 'Test2@'

        user = Users(username=username, email=email, password=password)
        user.generate_password_hash(password)
        db.session.add(user)
        db.session.commit()
        
        tester = self.client
        response = tester.post("/api/v1/login", json={'email': email, 'password': 'invalid'})
        self.assertEqual(response.status_code, 401)

"""
Code Analysis

Main functionalities:
The LoginOut class is responsible for handling the logout functionality of the application. It uses the Flask-JWT-Extended library to ensure that the user is authenticated before logging out. Once the user is authenticated, the JWT token is added to the blacklist to prevent it from being used again. The class returns a response indicating that the user has been logged out successfully.

Methods:
- post(): This method is responsible for handling the HTTP POST request for logging out. It first checks if the user is authenticated using the @jwt_required decorator. If the user is authenticated, the JWT token is retrieved and added to the blacklist. Finally, a response is returned indicating that the user has been logged out successfully.

Fields:
- None.
"""
class TestLoginOut(unittest.TestCase):
    def create_app(self):
        app = create_app(config_name="testing")
        return app

    def setUp(self):
        self.app = self.create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    # Tests that a user can successfully logout with a valid JWT token
    def test_successful_logout(self):
        username = 'test'
        email = 'test@test.com'
        password = 'Test2@'
        
        # create a user
        user = Users(username=username, email=email, password=password)
        user.generate_password_hash(password)
        db.session.add(user)
        db.session.commit()
        
        # tester client
        tester = self.client
        
        # login the user
        response = tester.post("/api/v1/login", json={'email': email, 'password': password})
        res = response.json
        access_token = res["data"]["access_token"]
       
        # logout the user
        response = tester.post('/api/v1/logout', headers={'Authorization': f'Bearer {access_token}'})
        res = response.json
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['status'], 200)
        self.assertEqual(res['message'], 'You have been logged Out successfully')
        
        
    # Tests that a user cannot logout with an invalid JWT token
    def test_invalid_logout(self):
        username = 'test'
        email = 'test@test.com'
        password = 'Test2@'
        
        # create a user
        user = Users(username=username, email=email, password=password)
        user.generate_password_hash(password)
        db.session.add(user)
        db.session.commit()
        
        # tester client
        tester = self.client
        
        # login the user
        response = tester.post("/api/v1/login", json={'email': email, 'password': password})
        res = response.json
        access_token = res["data"]["access_token"]
       
        # logout the user with an invalid token
        response = tester.post('/api/v1/logout', headers={'Authorization': f'Bearer {access_token} invalid'})
        res = response.json
        self.assertEqual(response.status_code, 422)
