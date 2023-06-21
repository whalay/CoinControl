from flask import render_template
from flask import Blueprint

main = Blueprint("main", __name__, template_folder='templates', static_folder='static')

@main.route('/', methods=["POST","GET"])
def home():
    return render_template('home.html')

@main.route('/dashboard', methods=["GET"])
def dashboard():
    pass



