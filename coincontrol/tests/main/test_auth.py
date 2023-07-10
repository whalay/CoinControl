import unittest
from coincontrol.extensions import db
from coincontrol.models import Users
from coincontrol import create_app
from flask_jwt_extended import create_access_token
from flask import request

"""
Code Analysis

Main functionalities:
The Register route is responsible for handling user registration. It receives user data and validates it on submit using the RegistrationForm class, and creates a new user in the Users table of the database.
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
        
    """
    Tests that a user can successfully register with valid data
    """
    def test_successful_registration(self):
        
        username = "testuser"
        email = "testuser@test.com",
        password = "password",
        confirm_password = "password"
        
        data = {
            "username": username,
            "email": email,
            "password": password,
            "confirm_password": confirm_password
        }
        
        tester = self.client
        response = tester.post("/register", json=data, follow_redirects=True)        
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'A confirmation email has been sent to your email address.', response.data)
   
         
    def test_empty_form_submission(self):
        # Test empty form submission
        tester = self.client
        response = tester.post("/register", data={}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"This field is required.", response.data)
        
    def test_invalid_form_submission(self):
        # Test invalid form submission
        username = "testuser"
        email = "invalid-email",
        password = "pass",
        confirm_password = "password"
        
        data = {
            "username": username,
            "email": email,
            "password": password,
            "confirm_password": confirm_password
        }
        
        tester = self.client
        response = tester.post("/register", json=data, follow_redirects=True)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Invalid email address.", response.data)
        self.assertIn(b"Password must match confirm password", response.data)
        self.assertIn(b"Password must include at least one uppercase letter, one lowercase letter, one number, and one special character", response.data)
        


class TestLogin(unittest.TestCase):
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
    pass


class TestLoginOut(unittest.TestCase):
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
    pass


    # def test_user_registration(self):
    #     # Testing user registration process
    #     user = Users(
    #         username="testuser", password="testpassword", email="test@gmail.com"
    #     )
    #     db.session.add(user)
    #     db.session.commit()

    #     tester = self.client
    #     response = tester.post(
    #         "/register",
    #         json={
    #             "username": "testuser",
    #             "email": "test@gmail.com",
    #             "password": "testpassword",
    #             "confirm_password": "testpassword"  
    #         },
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     # self.assertIn(b'User registered successfully', response.data)







    def test_user_login(self):
        # Testing user login process
        username = "testuser"
        email = "test@gmail.com"
        password = "testpassword"
        user = Users(username=username, email=email, password=password)
        user.generate_password_hash(password)
        db.session.add(user)
        db.session.commit()

        # login
        tester = self.client
        response = tester.post(
            "/login", json={"email": email, "password": password}, follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

        # log out
        response = tester.post("/logout", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_confirm_token(self):
        # Testing token confirmation process
        username = "testuser"
        password = "testpassword"
        email = "testemail@gmail.com"
        user = Users(username=username, password=password, email=email)
        user.generate_password_hash(password)

        db.session.add(user)
        db.session.commit()

        # To send a confirmation token to a user
        user = Users.query.filter_by(email=email).first()
        user_id = user.user_id

        # generate a confirmation_token
        token = create_access_token(identity=user_id)

        # perform token verification
        with self.app.test_request_context():
            from flask_jwt_extended import decode_token

            decoded_token = decode_token(token)
      
        tester = self.client
        response = tester.get(f'/confirm/{token}', follow_redirects=True)
        
        # verify the decoded token
        self.assertEqual(decoded_token["sub"], user_id)
        self.assertEqual(response.status_code, 200)
        
        
        
        



if __name__ == "__main__":
    unittest.main()
