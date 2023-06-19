from flask import Flask
from app.config import config
from app.main import main
from app.extensions import db

def create_app(config_name='development'):
    app = Flask(__name__)
    # setting up configuration from the development object
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
   
    # mainblueprint registration
    app.register_blueprint(main)
   
    # initialize the db 
    db.init_app(app)
    return app

