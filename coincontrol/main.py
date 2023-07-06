from flask import render_template, redirect, url_for
from flask import Blueprint, flash
from flask_login import login_required, current_user
from coincontrol.decorators import check_confirmed
main = Blueprint("main", __name__, template_folder='templates', static_folder='static')

@main.route('/', methods=["GET"])
def home():
    return render_template('home.html')

@main.route('/dashboard', methods=["GET"])
@login_required
@check_confirmed
def dashboard():
   
    return render_template('dashboard/dashboard.html')

# Expenses management route
@main.route('/expenses', methods=["GET","POST"])
@login_required
def expenses():
    pass

@main.route('/expenses/<int:id>', methods=["GET"])
@login_required
def get_expenses():
    pass

@main.route('/expenses/<int:id>', methods=["POST"])
@login_required
def update_expenses():
    pass

@main.route('/expenses/<int:id>', methods=["POST"])
@login_required
def delete_expenses():
    pass

# ---------------------------------------------------------------------------------------

# Income management route
@main.route('/income', methods=["GET","POST"])
@login_required
def income():
    pass

@main.route('/income/<int:id>', methods=["GET"])
@login_required
def get_income():
    pass

@main.route('/income/<int:id>', methods=["POST"])
@login_required
def update_income():
    pass

@main.route('/income/<int:id>', methods=["POST"])
@login_required
def delete_income():
    pass

# ---------------------------------------------------------------------------------------

# Budgets management route
@main.route('/budgets', methods=["GET","POST"])
@login_required
def budgets():
    pass

@main.route('/budgets/<int:id>', methods=["GET"])
@login_required
def get_budgets():
    pass

@main.route('/budgets/<int:id>', methods=["POST"])
@login_required
def update_budgets():
    pass

@main.route('/budgets/<int:id>', methods=["POST"])
@login_required
def delete_budgets():
    pass

# ---------------------------------------------------------------------------------------

# Report and Analytics management route
@main.route('/reports/expenses', methods=["GET"])
@login_required
def reports_expenses():
    pass

@main.route('/reports/income', methods=["GET"])
@login_required
def reports_income():
    pass

@main.route('/reports/budgets', methods=["GET"])
@login_required
def reports_budgets():
    pass
# ---------------------------------------------------------------------------------------


# Account Settings and security route
@main.route('/profile', methods=["GET", "POST"])
@login_required
def profile():
    pass