from flask import Blueprint

auth = Blueprint("auth", __name__, template_folder='templates', static_folder='static')

@auth.route('/register', methods=["POST"])
def register():
    return "pass"

@auth.route('/login', methods=["POST"])
def login():
    return "pass"

@auth.route('/logout', methods=["POST"])
def logout():
    return "pass"

