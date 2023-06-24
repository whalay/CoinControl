from flask_restful import Resource
from coincontrol.api.decorators import monitor

class Dashboard(Resource):
    response = {"status":400}
    
    @monitor
    def get(self):
        # app logic written here
        pass

class Expenses(Resource):
    response = {"status":400}
    
    @monitor
    def get(self):
        # app logic written here
        pass
    
    @monitor
    def post(self):
        # app logic written here
        pass
    

class ExpensesById(Resource):
    response = {"status":400}
    
    @monitor
    def get(self):
        # app logic written here
        pass
    
    @monitor
    def put(self):
        # app logic written here
        pass  
    
    @monitor
    def delete(self):
        # app logic written here
        pass  
    
class Income(Resource):
    response = {"status":400}
    
    @monitor
    def get(self):
        # app logic written here
        pass
    
    @monitor
    def post(self):
        # app logic written here
        pass  

class IncomeById(Resource):
    response = {"status":400}
    
    @monitor
    def get(self):
        # app logic written here
        pass
    
    @monitor
    def put(self):
        # app logic written here
        pass  
    
    @monitor
    def delete(self):
        # app logic written here
        pass 
    
class Budgets(Resource):
    response = {"status":400}
    
    @monitor
    def get(self):
        # app logic written here
        pass
    
    @monitor
    def post(self):
        # app logic written here
        pass  

class BudgetsById(Resource):
    response = {"status":400}
    
    @monitor
    def get(self):
        # app logic written here
        pass
    
    @monitor
    def put(self):
        # app logic written here
        pass  
    
    @monitor
    def delete(self):
        # app logic written here
        pass 

# Report management 
class ExpensesReport(Resource):
    response = {"status":400}
    
    @monitor
    def get(self):
        # app logic written here
        pass
    
class IncomeReport(Resource):
    response = {"status":400}
    
    @monitor
    def get(self):
        # app logic written here
        pass
    
class BudgetsReport(Resource):
    response = {"status":400}
    
    @monitor
    def get(self):
        # app logic written here
        pass
    
# Account management 
class Profile(Resource):
    response = {"status":400}
    
    @monitor
    def get(self):
        # app logic written here
        pass
    
    @monitor
    def put(self):
        # app logic written here
        pass
    
    
    