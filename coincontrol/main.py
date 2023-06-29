from flask import render_template
from flask import Blueprint

main = Blueprint("main", __name__, template_folder='templates', static_folder='static')

@main.route('/', methods=["GET"])
def home():
    return render_template('home.html')

@main.route('/dashboard', methods=["GET"])
def dashboard():
    pass

# Expenses management route
@main.route('/expenses', methods=["GET","POST"])
def expenses():
    pass

@main.route('/expenses/<int:id>', methods=["GET"])
def get_expenses():
    pass

@main.route('/expenses/<int:id>', methods=["POST"])
def update_expenses():
    pass

@main.route('/expenses/<int:id>', methods=["POST"])
def delete_expenses():
    pass

# ---------------------------------------------------------------------------------------

# Income management route
@main.route('/income', methods=["GET","POST"])
def income():
    pass

@main.route('/income/<int:id>', methods=["GET"])
def get_income():
    pass

@main.route('/income/<int:id>', methods=["POST"])
def update_income():
    pass

@main.route('/income/<int:id>', methods=["POST"])
def delete_income():
    pass

# ---------------------------------------------------------------------------------------

# Budgets management route
@main.route('/budgets', methods=["GET","POST"])
def budgets():
    pass

@main.route('/budgets/<int:id>', methods=["GET"])
def get_budgets():
    pass

@main.route('/budgets/<int:id>', methods=["POST"])
def update_budgets():
    pass

@main.route('/budgets/<int:id>', methods=["POST"])
def delete_budgets():
    pass

# ---------------------------------------------------------------------------------------

# Report and Analytics management route
@main.route('/reports/expenses', methods=["GET"])
def reports_expenses():
    pass

@main.route('/reports/income', methods=["GET"])
def reports_income():
    pass

@main.route('/reports/budgets', methods=["GET"])
def reports_budgets():
    pass
# ---------------------------------------------------------------------------------------


# Account Settings and security route
@main.route('/profile', methods=["GET", "POST"])
def profile():
    pass