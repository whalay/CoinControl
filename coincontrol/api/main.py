from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_restful import Api, Resource, request, url_for

from coincontrol.extensions import db
from coincontrol.forms import IncomeForm
from coincontrol.models import Budgets, Expenses, Incomes

from .decorators import monitor

api_main = Blueprint("api_main", __name__)
api = Api(api_main, prefix="/api/v1")


class Dashboard(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass


api.add_resource(Dashboard, "/dashboard")


class Expenses(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass

    @monitor
    @jwt_required(fresh=True)
    def post(self):
        # app logic written here
        pass


api.add_resource(Expenses, "/expenses")


class ExpensesById(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass

    @monitor
    @jwt_required(fresh=True)
    def put(self):
        # app logic written here
        pass

    @monitor
    @jwt_required(fresh=True)
    def delete(self):
        # app logic written here
        pass


api.add_resource(ExpensesById, "/expenses/<int:id>")


class Income(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        try:
            income = Incomes.query.all()
            if income:
                response = {
                    "status": 200,
                    "message": "Income fetched successfully",
                    "data": {
                        "status": "success",
                        "income": income.amount
                    }
                }
                return response, 200
            else:
                response = {
                    "status": 400,
                    "message": "No income found",
                    "data": {
                        "status": "failed",
                    }
                }
                return response, 400
        except Exception as e:
            print(e) 

    @monitor
    @jwt_required(fresh=True)
    def post(self):
        # app logic written here
        try:
            user_data = request.get_json()
            user_id = user_data.get("user_id", "")
            amount = user_data.get("amount", "")
            form = IncomeForm()
            if form.validate():
                form.user_id.data, form.amount.data = user_id, amount
                user_id, amount = form.user_id.data, form.amount.data

                income = Incomes(user_id=user_id, amount=amount)
                db.session.add(income)
                db.commit()
                response = {
                    "status": 200,
                    "message": "Income added successfully",
                    "data": {
                        "status": "success",
                        "amount": amount
                    }
                }
                return response, 200
            else:
                response = {
                    "status": 400,
                    "message": "Invalid form data",
                    "data": {
                        "status": "failed",
                        "error": form.errors ,
                    }
                }
        except Exception as e:
            print(e)


api.add_resource(Income, "/income")


# class IncomeById(Resource):
#     response = {"status": 400}

#     @monitor
# @jwt_required(fresh=True)
#     def get(self):
#         # app logic written here
#         pass

#     @monitor
# @jwt_required(fresh=True)
#     def put(self):
#         # app logic written here
#         pass

#     @monitor
# @jwt_required(fresh=True)
#     def delete(self):
#         # app logic written here
#         pass


# api.add_resource(IncomeById, "/income/<int:id>")


class Budgets(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass

    @monitor
    @jwt_required(fresh=True)
    def post(self):
        # app logic written here
        pass


api.add_resource(Budgets, "/budgets")


class BudgetsById(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass

    @monitor
    @jwt_required(fresh=True)
    def put(self):
        # app logic written here
        pass

    @monitor
    @jwt_required(fresh=True)
    def delete(self):
        # app logic written here
        pass


api.add_resource(BudgetsById, "/budgets/<int:id>")


# Report management
class ExpensesReport(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass


api.add_resource(ExpensesReport, "/reports/expenses")


class IncomeReport(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass


api.add_resource(IncomeReport, "/reports/income")


class BudgetsReport(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass


api.add_resource(BudgetsReport, "/reports/budgets")


# Account management
class Profile(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass

    @monitor
    @jwt_required(fresh=True)
    def put(self):
        # app logic written here
        pass


api.add_resource(Profile, "/profile")
