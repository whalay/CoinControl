from flask import Blueprint
from flask_jwt_extended import current_user, jwt_required
from flask_restful import Api, Resource, request

from coincontrol.api.decorators import monitor, user_required
from coincontrol.extensions import db
from coincontrol.forms import BudgetForm, EditBudgetForm, ExpenseForm, IncomeForm
from coincontrol.models import Budgets, Expenses, Incomes

api_user_bp = Blueprint("api_user_bp", __name__)
api = Api(api_user_bp, prefix="/api/v1")


class UserDashboard(Resource):
    response = {"status": 400}

    @monitor
    @jwt_required(fresh=True)
    @user_required
    def get(self):
        # app logic written here
        pass


api.add_resource(UserDashboard, "/dashboard")


class UserExpenses(Resource):
    @monitor
    @jwt_required(fresh=True)
    @user_required
    def get(self):
        # app logic written here
        try:
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per_page", 4, type=int)
            expenses = Expenses.query.filter_by(user_id=current_user.user_id).paginate(
                page=page, per_page=per_page
            )
            if expenses:
                data = []
                for expense in expenses.items:
                    data.append(
                        {
                            "expense_id": expense.expenses_id,
                            "user_id": expense.user_id,
                            "budget_id": expense.budget_id,
                            "amount": expense.amount,
                            "description": expense.description,
                            "transaction_type": expense.transaction_type,
                            "account_number": expense.account_number,
                            "bank_name": expense.bank_name,
                            "date_created": expense.date_created.strftime("%Y-%m-%d"),
                        }
                    )
                meta = {
                    "page": expenses.page,
                    "pages": expenses.pages,
                    "total_count": expenses.total,
                    "prev_page": expenses.prev_num,
                    "next_page": expenses.next_num,
                    "has_next": expenses.has_next,
                    "has_prev": expenses.has_prev,
                }
                response = {
                    "status": 200,
                    "message": "Expenses fetched successfully",
                    "data": {"status": "success", "data": data},
                    "meta": meta,
                }
                return response, 200
            else:
                response = {
                    "status": 200,
                    "message": "No Expenses found",
                    "data": {
                        "status": "success",
                    },
                }
                return response, 200
        except Exception as e:
            print(e)

    @monitor
    @jwt_required(fresh=True)
    @user_required
    def post(self):
        # app logic written here
        try:
            user_data = request.get_json()
            name = user_data.get("name", "")
            amount = float(user_data.get("amount", ""))
            description = user_data.get("description")
            account_number = user_data.get("account_number")
            bank_name = user_data.get("bank_name").lower()
            transaction_type = "withdrawal"
            form = ExpenseForm()
            if form.validate():
                name = form.name.data
                description = form.description.data
                amount = form.amount.data
                account_number = form.account_number.data
                bank_name = form.bank_name.data
                budget = Budgets.query.filter_by(name=name).first()
                if budget is not None:
                    expense = Expenses(
                        user_id=current_user.user_id,
                        budget_id=budget.budget_id,
                        amount=amount,
                        description=description,
                        account_number=account_number,
                        bank_name=bank_name,
                        transaction_type=transaction_type,
                    )
                    budget.amount -= amount
                    db.session.add(expense)
                    db.session.commit()
                    response = {
                        "status": 201,
                        "message": "Withdrawal successfull",
                        "data": {
                            "status": "success",
                            "from": name,
                            "to": bank_name,
                            "amount": amount,
                            "description": description,
                            "transaction_type": transaction_type,
                        },
                    }
                    return response, 201
            else:
                response = {
                    "status": 400,
                    "mesage": "Withdrawal failed",
                    "data": {
                        "status": "failed",
                        "error": form.errors,
                    },
                }
                return response, 400
        except Exception as e:
            print(e)


api.add_resource(UserExpenses, "/expenses")


class UserIncome(Resource):
    @monitor
    @jwt_required(fresh=True)
    @user_required
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
                    "status": 404,
                    "message": "No income found",
                }
                return response, 404
        except Exception as e:
            print(e)

    @monitor
    @jwt_required(fresh=True)
    @user_required
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
                    "status": 409,
                    "message": "User Income already exists",
                }
                return response, 409
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

    @monitor
    @jwt_required(fresh=True)
    @user_required
    def put(self):
        # app logic written here
        try:
            user_data = request.get_json()
            amount = float(user_data.get("amount", ""))
            form = IncomeForm()
            if form.validate():
                amount = form.amount.data
                existing_user_income = Incomes.query.filter_by(
                    user_id=current_user.user_id
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


api.add_resource(UserIncome, "/income")


class UserBudgets(Resource):
    @monitor
    @jwt_required(fresh=True)
    @user_required
    def get(self):
        # app logic written here
        try:
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per_page", 4, type=int)
            budgets = Budgets.query.filter_by(user_id=current_user.user_id).paginate(
                page=page, per_page=per_page
            )
            if budgets:
                data = []
                for budget in budgets.items:
                    data.append(
                        {
                            "id": budget.budget_id,
                            "name": budget.name,
                            "amount": budget.amount,
                            "date_created": budget.date_created.strftime("%Y-%m-%d"),
                        }
                    )
                meta = {
                    "page": budgets.page,
                    "pages": budgets.pages,
                    "total_count": budgets.total,
                    "prev_page": budgets.prev_num,
                    "next_page": budgets.next_num,
                    "has_next": budgets.has_next,
                    "has_prev": budgets.has_prev,
                }
                response = {
                    "status": 200,
                    "message": "Budgets fetched successfully",
                    "data": {"status": "success", "data": data},
                    "meta": meta,
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
    @user_required
    def post(self):
        # app logic written here
        try:
            user_data = request.get_json()
            name = user_data.get("name", "")
            amount = float(user_data.get("amount", ""))
            income = Incomes.query.filter_by(user_id=current_user.user_id).first()
            form = BudgetForm()
            if amount:
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

            if form.validate():
                name, amount = (
                    form.name.data.strip().replace(" ", "-").lower(),
                    form.amount.data,
                )
                budget = Budgets(user_id=current_user.user_id, name=name, amount=amount)
                income.amount -= amount

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
                return response, 400

        except Exception as e:
            print(e)


api.add_resource(UserBudgets, "/budgets")


class UserBudgetsById(Resource):
    @monitor
    @jwt_required(fresh=True)
    @user_required
    def get(self, id):
        # app logic written here
        try:
            budget = Budgets.query.filter_by(
                budget_id=id, user_id=current_user.user_id
            ).first()
            if budget is not None:
                response = {
                    "status": 200,
                    "message": "Budget fetched successfully",
                    "data": {
                        "status": "success",
                        "id": budget.budget_id,
                        "user_id": budget.user_id,
                        "name": budget.name,
                        "date_created": budget.date_created.strftime("%Y-%m-%d"),
                    },
                }
                return response, 200
            else:
                response = {
                    "status": 404,
                    "message": "Budget not found",
                }
                return response, 404
        except Exception as e:
            print(e)

    @monitor
    @jwt_required(fresh=True)
    @user_required
    def put(self, id):
        # app logic written here
        try:
            budget = Budgets.query.filter_by(
                budget_id=id, user_id=current_user.user_id
            ).first()
            income = Incomes.query.filter_by(user_id=current_user.user_id).first()

            if budget is not None:
                user_data = request.get_json()
                name = user_data.get("name", "")
                amount = float(user_data.get("amount", ""))
                if amount > income.amount:
                    response = {"status": 400, "message": "Insufficient balance"}
                    return response, 400
                form = EditBudgetForm()
                if form.validate():
                    name, amount = (
                        form.name.data.strip().replace(" ", "-").lower(),
                        form.amount.data,
                    )
                    new_income = income.amount - amount
                    print(new_income)
                    new_budget_balance = budget.amount + amount
                    print(new_budget_balance)
                    income.amount = new_income
                    budget.name = name
                    budget.amount = new_budget_balance

                    db.session.commit()
                    response = {
                        "status": 200,
                        "message": "Budget updated successfully",
                        "data": {
                            "status": "success",
                            "name": name,
                            "amount": amount,
                        },
                    }
                    return response, 200
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
            else:
                response = {"status": 404, "message": "Budget not found"}
                return response, 404
        except Exception as e:
            print(e)

    @monitor
    @jwt_required(fresh=True)
    @user_required
    def delete(self, id):
        # app logic written here
        try:
            budget = Budgets.query.filter_by(
                budget_id=id, user_id=current_user.user_id
            ).first()
            if budget is not None:
                db.session.delete(budget)
                db.session.commit()
                response = {"status": 200, "message": "Budget deleted successfully"}
                return response, 200
            else:
                response = {"status": 404, "message": "Budget not found"}
                return response, 404
        except Exception as e:
            print(e)


api.add_resource(UserBudgetsById, "/budgets/<int:id>")
