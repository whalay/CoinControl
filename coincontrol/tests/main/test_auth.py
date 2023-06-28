import unittest
from coincontrol.extensions import db
from coincontrol.models import *
from coincontrol import create_app 


class AuthTestCase(unittest.TestCase):
   
    def create_app(self):
        #Creating a test flask application 
        #Which takes in a parameter called testing which is passed as an argument to the config_name variable
        app = create_app(config_name='testing')
        return app
    
    def setUp(self):
        #Creating and configuring the test database
        self.app = self.create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)
        
    def tearDown(self):
        #Cleaning up the test database
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_user_registration(self):
        # Testing user registration process 
        user = Users(username='testuser', password='testpassword', email='test@gmail.com')
        db.session.add(user)
        db.session.commit()
        
        tester = self.client
        response = tester.post('/register', json={'username': 'testuser', 'password': 'testpassword', 'email': 'test@gmail.com'})
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'User registered successfully', response.data)
    
    def test_user_login(self):
        # Testing user login process
        user = Users(username='newuser', password='newpassword', email='newuser@gmail.com')
        db.session.add(user)
        db.session.commit()
        
        #login
        tester = self.client
        response = tester.post('/login', json={'email': 'newuser@gmail.com', 'password': 'newpassword'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        #log out
        response = tester.post('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        

if __name__ == '__main__':
    unittest.main()