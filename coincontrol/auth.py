from flask import Blueprint
from flask import render_template, redirect

auth = Blueprint("auth", __name__, template_folder='templates', static_folder='static')

@auth.route('/register', methods=["GET", "POST"])
def register():
    return render_template("auth/register.html")

@auth.route('/login', methods=["GET", "POST"])
def login():
    return render_template("auth/login.html")

@auth.route('/logout', methods=["GET", "POST"])
def logout():
    return "pass"



# Token confirmation route
@auth.route('/confirm/<token>', methods=["GET"])
def confirm_token(token):
    return "token"