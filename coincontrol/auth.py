from flask import Blueprint, session
from flask import request, render_template, redirect, url_for, flash
from coincontrol.forms import RegistrationForm, LoginForm
from coincontrol.extensions import bcrypt
from coincontrol.models import Users
from coincontrol.extensions import db
from flask_login import login_required, login_user, logout_user, current_user
from coincontrol.token import generate_confirmation_token, check_confirm_token
from datetime import datetime
from coincontrol.email import send_email
from itsdangerous import SignatureExpired 
from coincontrol.decorators import check_confirmed

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

        db.session.add(user)
        db.session.commit()
        
        token = generate_confirmation_token(user.email)
        confirm_url = url_for('auth.confirm_token', token=token, _external=True)
        subject = "CoinControl Email Confirmation"
        text = """\
            Thank you for registering with CoinControl
            """
        html = f"""\
            <html>
            <body>
                <p>Hi,<br>
                How are you?<br>
                <p>Welcome! Thanks for signing up. Please follow this link to activate your account:</p><br>
                <p><a href="{ confirm_url }">{ confirm_url }</a></p>
                </p>
            </body>
            </html>
            """

        send_email(email, subject, text, html)
        
        login_user(user)
        flash("A confirmation email has been sent to your email address.")
        return redirect(url_for("auth.unconfirmed"))

    return render_template("auth/register.html", form=form)

@auth.route('/unconfirmed', methods=["GET", "POST"])
@login_required
def unconfirmed():
    if current_user.verified:
        return redirect(url_for('main.home'))
    return render_template('auth/unconfirmed.html')


# Token confirmation route
@auth.route('/confirm/<token>', methods=["GET"])
@login_required
def confirm_token(token):
    try:
        email = check_confirm_token(token)
       
    except SignatureExpired:
        flash('The confirmation link is invalid or has expired.')
        return redirect(url_for('main.home'))
    user = Users.query.filter_by(email=email).first()
    if user.verified:
        flash('Account already verified. Please login.')
    else:
        user.verified = True
        user.date_verified = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have verified your account. Thanks!')
    return redirect(url_for('main.home'))


@auth.route('/resend-token', methods=["GET"])
@login_required
def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for('auth.confirm_token', token=token, _external=True)
    subject = "CoinControl Resend Email Confirmation"
    text = """\
        Thank you for registering with CoinControl
        """
    html = f"""\
        <html>
        <body>
            <p>Hi,<br>
            How are you?<br>
            <p>Welcome! Thanks for signing up. Please follow this link to activate your account:</p><br>
            <p><a href="{ confirm_url }">{ confirm_url }</a></p>
            </p>
        </body>
        </html>
        """

    send_email(current_user.email, subject, text, html)
    flash('A new confirmation email has been sent.')
    return redirect(url_for('auth.unconfirmed'))

@auth.route('/login', methods=["GET", "POST"])
def login():
    
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = form.remember.data
       
        user = Users.query.filter_by(email=email).first()
        user_password = user.password
        password_check = bcrypt.check_password_hash(user_password, password)
            
        if user is not None and password_check:
            login_user(user, remember=remember)
            flash('logged in successfully')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("main.dashboard"))
        else:
            flash("Login Unsuccessful. Please check username and password")

    return render_template("auth/login.html", form=form)



@auth.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return  redirect(url_for("auth.login"))





@auth.route('/admin', methods=["GET"])
@login_required
@check_confirmed
def admin():
    if current_user.is_admin != True:
        flash('You need to be an admin to access this page')
        return redirect(url_for('auth.login'))
    return render_template('dashboard/admin_dashboard.html')

