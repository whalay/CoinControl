from coincontrol.extensions import db
from datetime import datetime
from coincontrol.extensions import bcrypt


class Users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    verified = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    date_verified = db.Column(db.DateTime, index=True)
    

    def generate_password_hash(self, password):
        self.password = bcrypt.generate_password_hash(password, 10)

    def is_verified(self, token):
        self.verified = True

    def __repr__(self):
        return f"Users(username:'{self.username}', email:'{self.email}')"


class Categories(db.Model):
    __tablename__ = "categories"
    category_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    category_name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return (
            f"Categories(user_id:{self.user_id}, category_name:'{self.category_name}')"
        )


class Incomes(db.Model):
    __tablename__ = "incomes"
    income_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    amount = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __refr__(self):
        return f"Incomes(user_id:{self.user_id},amount:{self.amount})"


class Budgets(db.Model):
    __tablename__ = "budgets"
    budget_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    categories_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"))
    amount = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    date_ended = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __refr__(self):
        return f"Budgets(user_id:{self.user_id}, categories_id:{self.categories_id}, amount:{self.amount})"


class Expenses(db.Model):
    __tablename__ = "expenses"
    expenses_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    categories_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"))
    amount = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=True)

    def __refr__(self):
        return f"Expenses(user_id:{self.user_id}, categories_id:{self.categories_id}, amount:{self.amount})"
