from datetime import datetime

from flask_login import UserMixin

from coincontrol.extensions import bcrypt, db
from coincontrol.helpers import generate_uuid

from sqlalchemy import LargeBinary
class Users(UserMixin, db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    alternative_id = db.Column(db.String(36), default=generate_uuid)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(LargeBinary, nullable=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    verified = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    date_verified = db.Column(db.DateTime, index=True)
    budgets = db.relationship("Budgets", back_populates="users")
    expenses = db.relationship("Expenses", back_populates="users")
    incomes = db.relationship("Incomes", back_populates="users")

    def generate_password_hash(self, password):
        self.password = bcrypt.generate_password_hash(password, 10)

    def is_verified(self, token):
        self.verified = True

    def get_id(self):
        try:
            return str(self.user_id)
        except Exception as e:
            return e

    def __repr__(self):
        return f"Users(username:'{self.username}', email:'{self.email}')"


class Incomes(db.Model):
    __tablename__ = "incomes"
    income_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    amount = db.Column(db.Float, nullable=True, default=0.0)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    users = db.relationship("Users", back_populates="incomes")

    def __refr__(self):
        return f"Incomes(user_id:{self.user_id},amount:{self.amount})"


class Budgets(db.Model):
    __tablename__ = "budgets"
    budget_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    date_ended = db.Column(db.DateTime, index=True, nullable=True)
    users = db.relationship("Users", back_populates="budgets")
    expenses = db.relationship("Expenses", back_populates="budget")

    def __refr__(self):
        return f"Budgets(user_id:{self.user_id}, amount:{self.amount})"


class Expenses(db.Model):
    __tablename__ = "expenses"
    expenses_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    budget_id = db.Column(db.Integer, db.ForeignKey("budgets.budget_id"))
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    account_number = db.Column(db.String(20), nullable=False)
    bank_name = db.Column(db.String(20), nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    users = db.relationship("Users", back_populates="expenses")
    budget = db.relationship("Budgets", back_populates="expenses")

    def __refr__(self):
        return f"Expenses(user_id:{self.user_id}, budget_id:{self.budget_id}, amount:{self.amount})"


def create_income_for_user(user_id) -> None:
    income = Incomes(user_id=user_id)
    db.session.add(income)
    db.session.commit()
