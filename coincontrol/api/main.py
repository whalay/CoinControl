from flask_restful import Api, Resource, url_for
from .decorators import monitor
from flask import Blueprint


api_main = Blueprint("api_main", __name__)
api = Api(api_main, prefix="/api/v1")


class Dashboard(Resource):
    response = {"status": 400}

    @monitor
    def get(self):
        # app logic written here
        pass


api.add_resource(Dashboard, "/dashboard")


class Expenses(Resource):
    response = {"status": 400}

    @monitor
    def get(self):
        # app logic written here
        pass

    @monitor
    def post(self):
        # app logic written here
        pass


api.add_resource(Expenses, "/expenses")


class ExpensesById(Resource):
    response = {"status": 400}

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


api.add_resource(ExpensesById, "/expenses/<int:id>")


class Income(Resource):
    response = {"status": 400}

    @monitor
    def get(self):
        # app logic written here
        pass

    @monitor
    def post(self):
        # app logic written here
        pass


api.add_resource(Income, "/income")


class IncomeById(Resource):
    response = {"status": 400}

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


api.add_resource(IncomeById, "/income/<int:id>")


class Budgets(Resource):
    response = {"status": 400}

    @monitor
    def get(self):
        # app logic written here
        pass

    @monitor
    def post(self):
        # app logic written here
        pass


api.add_resource(Budgets, "/budgets")


class BudgetsById(Resource):
    response = {"status": 400}

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


api.add_resource(BudgetsById, "/budgets/<int:id>")


# Report management
class ExpensesReport(Resource):
    response = {"status": 400}

    @monitor
    def get(self):
        # app logic written here
        pass


api.add_resource(ExpensesReport, "/reports/expenses")


class IncomeReport(Resource):
    response = {"status": 400}

    @monitor
    def get(self):
        # app logic written here
        pass


api.add_resource(IncomeReport, "/reports/income")


class BudgetsReport(Resource):
    response = {"status": 400}

    @monitor
    def get(self):
        # app logic written here
        pass


api.add_resource(BudgetsReport, "/reports/budgets")


# Account management
class Profile(Resource):
    response = {"status": 400}

    @monitor
    def get(self):
        # app logic written here
        pass

    @monitor
    def put(self):
        # app logic written here
        pass


api.add_resource(Profile, "/profile")
