from flask import Flask
from coincontrol.config import config
from coincontrol.auth import auth
from coincontrol.main import main
from coincontrol.extensions import db
from flask_restful import Api
from coincontrol.api.auth import api_auth
from coincontrol.api.main import api_main
from coincontrol.auth import auth
from coincontrol.main import main

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
   
    
    
    # initialize the db 
    db.init_app(app)
    
    return app

