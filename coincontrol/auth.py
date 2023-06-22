from flask import Blueprint

auth = Blueprint("auth", __name__, template_folder='templates', static_folder='static')

@auth.route('/register', methods=["POST"])
def register():
    pass

@auth.route('/login', methods=["POST"])
def login():
    pass

@auth.route('/logout', methods=["POST"])
def logout():
    pass

