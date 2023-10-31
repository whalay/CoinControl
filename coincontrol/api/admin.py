from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_restful import Api, Resource, request, url_for

from coincontrol.api.decorators import admin_required, monitor
from coincontrol.extensions import db
from coincontrol.forms import IncomeForm
from coincontrol.models import Budgets, Expenses, Incomes, Users
from flask_jwt_extended import current_user

api_admin_bp = Blueprint("api_admin_bp", __name__)
api = Api(api_admin_bp, prefix="/api/v1/admin")


class AdminDashboard(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass


api.add_resource(AdminDashboard, "/dashboard")


class AdminExpenses(Resource):
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


api.add_resource(AdminExpenses, "/expenses")


class AdminExpensesById(Resource):
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


api.add_resource(AdminExpensesById, "/expenses/<int:id>")


class AdminIncome(Resource):
    @monitor
    @jwt_required(fresh=True)
    @admin_required
    def get(self):
        # app logic written here
        try:
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per_page", 4, type=int)
            incomes = Incomes.query.order_by(Incomes.user_id.desc()).paginate(
                page=page, per_page=per_page
            )
            if incomes:
                print("sam")
                data = []
                for income in incomes.items:
                    data.append(
                        {
                            "income_id": income.income_id,
                            "user_id": income.user_id,
                            "amount": income.amount,
                            "date_created": income.date_created.strftime("%Y-%m-%d"),
                        }
                    )
                meta = {
                    "page": incomes.page,
                    "pages": incomes.pages,
                    "total_count": incomes.total,
                    "prev_page": incomes.prev_num,
                    "next_page": incomes.next_num,
                    "has_next": incomes.has_next,
                    "has_prev": incomes.has_prev,
                }
                response = {
                    "status": 200,
                    "message": "Income fetched successfully",
                    "data": {"status": "success", "data": data},
                    "meta": meta,
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
                return response, 400
        except Exception as e:
            print(e)

api.add_resource(AdminIncome, "/income")


class AdminIncomeById(Resource):
    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass

    @monitor
    @jwt_required(fresh=True)
    def put(self, id):
        # app logic written here
        try:
            user_data = request.get_json()
            amount = float(user_data.get("amount", ""))
            user = Users.query.filter_by(user_id=id).first()
            form = IncomeForm()
            if form.validate():
                amount = form.amount.data
                existing_user_income = Incomes.query.filter_by(
                    user_id=user.user_id
                ).first()
                existing_user_income.amount += amount
                db.session.commit()
                response = {
                    "status": 201,
                    "message": "Income top up successfull",
                    "data": {
                        "status": "success",
                        "amount": amount,
                        "available_balance": existing_user_income.amount,
                    },
                }
                return response, 201
            else:
                response = {
                    "status": 400,
                    "message": "Income top up failed",
                    "data": {
                        "status": "failed",
                        "error": form.errors,
                    },
                }
                return response, 400
        except Exception as e:
            print(e)
        pass

    @monitor
    @jwt_required(fresh=True)
    def delete(self):
        # app logic written here
        pass


api.add_resource(AdminIncomeById, "/income/<int:id>")


class AdminBudgets(Resource):
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


api.add_resource(AdminBudgets, "/budgets")


class AdminBudgetsById(Resource):
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


api.add_resource(AdminBudgetsById, "/budgets/<int:id>")


# Report management
class AdminExpensesReport(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass


api.add_resource(AdminExpensesReport, "/reports/expenses")


class AdminIncomeReport(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass


api.add_resource(AdminIncomeReport, "/reports/income")


class AdminBudgetsReport(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    def get(self):
        # app logic written here
        pass


api.add_resource(AdminBudgetsReport, "/reports/budgets")


# Account management
class AdminProfile(Resource):
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


api.add_resource(AdminProfile, "/profile")
