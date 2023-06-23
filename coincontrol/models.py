from coincontrol.extensions import db
from datetime import datetime


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80), unique= True, nullable=False)
    password = db.Column(db.String(60), nullable = False)
    email = db.Column(db.String(80), unique=True, nullable = False)
    verified = db.Column(db.Boolean, default=0)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"Users('username:{self.username}', 'email:{self.email}')"
        
class Categories(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    category_name = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f"Categories('user_id:{self.user_id}', 'category_name:{self.category_name}')"
    
class Incomes(db.Model):
    __tablename__ = 'incomes'
    income_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    amount = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __refr__(self):
        return f"Incomes('user_id:{self.user_id},'amount:{self.amount}')"
    
class Budgets(db.Model):
    __tablename__ = 'budgets'
    budget_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
    amount = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    date_ended = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class Expenses(db.Model):
    __tablename__ = 'expenses'
    expenses_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
    amount = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=True )
 
    