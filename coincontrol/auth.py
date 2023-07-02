from flask import Blueprint
from flask import request, render_template, redirect, url_for, flash
from coincontrol.forms import RegistrationForm, LoginForm
from flask_bcrypt import check_password_hash
from coincontrol.models import Users
from coincontrol.extensions import db

auth = Blueprint("auth", __name__, template_folder='templates', static_folder='static')

@auth.route('/register', methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = Users(username=username, email=email, password=password)
        user.generate_password_hash(password)
        print(user)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)

    

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