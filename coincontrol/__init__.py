from flask import Flask
from coincontrol.config import config
from coincontrol.auth import auth
from coincontrol.main import main
from coincontrol.extensions import db

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # setting up configuration from the development object
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
   
    # register blueprints here
    app.register_blueprint(auth)
    app.register_blueprint(main)
   
    # initialize the db 
    db.init_app(app)
    return app

