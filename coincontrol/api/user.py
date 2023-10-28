from flask import Blueprint
from flask_jwt_extended import current_user, jwt_required
from flask_restful import Api, Resource, request

from coincontrol.extensions import db
from coincontrol.forms import BudgetForm, IncomeForm
from coincontrol.models import Budgets, Expenses, Incomes

from .decorators import monitor

api_user_bp = Blueprint("api_user_bp", __name__)
api = Api(api_user_bp, prefix="/api/v1")


class UserDashboard(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass


api.add_resource(UserDashboard, "/dashboard")


class UserExpenses(Resource):
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


api.add_resource(UserExpenses, "/expenses")


class UserExpensesById(Resource):
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


api.add_resource(UserExpensesById, "/expenses/<int:id>")


class UserIncome(Resource):
    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        try:
            income = Incomes.query.filter_by(user_id=current_user.user_id).first()
            if income:
                response = {
                    "status": 200,
                    "message": "Income fetched successfully",
                    "data": {"status": "success", "income": income.amount},
                }
                return response, 200
            else:
                response = {
                    "status": 200,
                    "message": "No income found",
                    "data": {
                        "status": "success",
                    },
                }
                return response, 200
        except Exception as e:
            print(e)

    @monitor
    @jwt_required(fresh=True)
    def post(self):
        # app logic written here
        try:
            user_data = request.get_json()
            amount = float(user_data.get("amount", ""))
            existing_user_income = Incomes.query.filter_by(
                user_id=current_user.user_id
            ).first()
            if existing_user_income:
                response = {
                    "status": 400,
                    "message": "User Income already exists",
                    "data": {
                        "status": "failed",
                    },
                }
                return response, 400
            form = IncomeForm()
            if form.validate():
                form.amount.data = amount
                amount = form.amount.data
                income = Incomes(user_id=current_user.user_id, amount=amount)
                db.session.add(income)
                db.session.commit()
                response = {
                    "status": 201,
                    "message": "Income added successfully",
                    "data": {"status": "success", "amount": amount},
                }
                return response, 201
            else:
                response = {
                    "status": 400,
                    "message": "Invalid form data",
                    "data": {
                        "status": "failed",
                        "error": form.errors,
                    },
                }
                return response, 400
        except Exception as e:
            print(e)


api.add_resource(UserIncome, "/income")


class UserBudgets(Resource):
    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        try:
            budgets = Budgets.query.filter_by(user_id=current_user.user_id).first()
            if budgets:
                response = {
                    "status": 200,
                    "message": "Budgets fetched successfully",
                    "data": {
                        "status": "success",
                        "id": budgets.budget_id,
                        "name": budgets.name,
                        "amount": budgets.amount,
                        # "date_created": budgets.date_created,
                        # "date_ended": budgets.date_ended,
                    },
                }
                return response, 200
            else:
                response = {
                    "status": 200,
                    "message": "No budgets found",
                    "data": {
                        "status": "success",
                    },
                }
                return response, 200
        except Exception as e:
            print(e)

    @monitor
    @jwt_required(fresh=True)
    def post(self):
        # app logic written here
        try:
            user_data = request.get_json()
            name = user_data.get("name", "")
            amount = float(user_data.get("amount", ""))
            form = BudgetForm()
            if amount:
                income = Incomes.query.filter_by(user_id=current_user.user_id).first()
                if income is not None:
                    if income.amount < amount:
                        response = {
                            "status": 400,
                            "message": "Insufficient balance",
                            "data": {
                                "status": "failed",
                            },
                        }
                        return response, 400

            if form.validate:
                amount, name = form.amount.data, form.name.data
                budget = Budgets(user_id=current_user.user_id, name=name, amount=amount)
                db.session.add(budget)
                db.session.commit()
                response = {
                    "status": 201,
                    "message": "Budget added successfully",
                    "data": {"status": "sucess", "name": name, "amount": amount},
                }
                return response, 201
            else:
                response = {
                    "status": 400,
                    "message": "Invalid form data",
                    "data": {
                        "status": "failed",
                        "error": form.errors,
                    },
                }
        except Exception as e:
            print(e)


api.add_resource(UserBudgets, "/budgets")


class UserBudgetsById(Resource):
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


api.add_resource(UserBudgetsById, "/budgets/<int:id>")


# Report management
class UserExpensesReport(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass


api.add_resource(UserExpensesReport, "/reports/expenses")


class UserIncomeReport(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass


api.add_resource(UserIncomeReport, "/reports/income")


class UserBudgetsReport(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass


api.add_resource(UserBudgetsReport, "/reports/budgets")


# Account management
class UserProfile(Resource):
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


api.add_resource(UserProfile, "/profile")
