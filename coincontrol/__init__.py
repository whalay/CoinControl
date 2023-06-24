from flask import Flask
from coincontrol.config import config
from coincontrol.auth import auth
from coincontrol.main import main
from coincontrol.extensions import db
from flask_restful import Api
from coincontrol.api.auth import *
from coincontrol.api.main import *

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # setting up configuration from the development object
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
   
    # register blueprints here
    app.register_blueprint(auth)
    app.register_blueprint(main)
    
    # initialize the app
    api = Api(app, prefix='/api/v1')     
    api.add_resource(Register, '/register')
    api.add_resource(Login, '/login')
    api.add_resource(LoginOut, '/logout')
    api.add_resource(Dashboard, '/dashboard')
    api.add_resource(Expenses, '/expenses')
    api.add_resource(ExpensesById, '/expenses/<int:id>')
    api.add_resource(Income, '/income')
    api.add_resource(IncomeById, '/income/<int:id>')
    api.add_resource(Budgets, '/budgets')
    api.add_resource(BudgetsById, '/budgets/<int:id>')
    api.add_resource(ExpensesReport, '/reports/expenses')
    api.add_resource(IncomeReport, '/reports/income')
    api.add_resource(BudgetsReport, '/reports/budgets')
    api.add_resource(Profile, '/profile')
    
    
    
    
    
    # initialize the db 
    db.init_app(app)
    
    return app

