from flask import Blueprint
from flask import request, render_template, redirect, url_for, flash
from coincontrol.forms import RegistrationForm, LoginForm, ResetPasswordForm, EmailForm
from coincontrol.extensions import bcrypt
from coincontrol.models import Users
from coincontrol.extensions import db
from flask_login import login_required, login_user, logout_user, current_user
from coincontrol.token import generate_confirmation_token, check_confirm_token
from datetime import datetime
from coincontrol.email import (
    send_confirm_email,
    resend_confirm_email,
    send_passwordreset_email,
)
from itsdangerous import SignatureExpired, BadSignature
from coincontrol.decorators import check_confirmed

auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")


@auth.route("/register", methods=["GET", "POST"])
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
        confirm_url = url_for("auth.confirm_token", token=token, _external=True)

        send_confirm_email(
            email_receiver=email, user=user.username, confirm_url=confirm_url
        )

        login_user(user)
        flash("A confirmation email has been sent to your email address.")
        return redirect(url_for("auth.unconfirmed"))

    return render_template("auth/register.html", form=form)


@auth.route("/unconfirmed", methods=["GET", "POST"])
@login_required
def unconfirmed():
    if current_user.verified:
        return redirect(url_for("main.home"))
    return render_template("auth/unconfirmed.html")


# Token confirmation route
@auth.route("/confirm/<token>", methods=["GET"])
@login_required
def confirm_token(token):
    try:
        email = check_confirm_token(token)
    except SignatureExpired:
        flash("The confirmation link is invalid or has expired.")
        return redirect(url_for("main.home"))
    user = Users.query.filter_by(email=email).first()
    if user.verified:
        flash("Account already verified. Please login.")
    else:
        user.verified = True
        user.date_verified = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash(
            "You have verified your email, you can now login to your dashboard. Thanks!"
        )
    return redirect(url_for("main.home"))


@auth.route("/resend-token", methods=["GET"])
@login_required
def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for("auth.confirm_token", token=token, _external=True)
    resend_confirm_email(
        email_receiver=current_user.email,
        user=current_user.username,
        confirm_url=confirm_url,
    )
    flash("A new confirmation email has been sent.")
    return redirect(url_for("auth.unconfirmed"))


@auth.route("/login", methods=["GET", "POST"])
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
            flash("logged in successfully")
            next_page = request.args.get("next")
            return (
                redirect(next_page)
                if next_page
                else redirect(url_for("main.dashboard"))
            )
        else:
            flash("Login Unsuccessful. Please check username and password")

    return render_template("auth/login.html", form=form)


@auth.route("/forgotpassword", methods=["GET", "POST"])
def forgotpassword():
    form = EmailForm()
    if form.validate_on_submit():
        # verify if user exists
        user = Users.query.filter_by(email=form.email.data).first()
        form_email = form.email.data

        token = generate_confirmation_token(form_email)
        confirm_url = url_for("auth.confirmpassword", token=token, _external=True)

        send_passwordreset_email(
            email_receiver=form_email, user=user.username, confirm_url=confirm_url
        )
        flash(f"We just emailed {form_email} with instructions to reset your password")
        return redirect(url_for("auth.login"))
    return render_template("auth/forgotpassword.html", form=form)


@auth.route("/confirmpassword/<token>", methods=["GET", "POST"])
def confirmpassword(token):
    try:
        email = check_confirm_token(token)
    except SignatureExpired:
        flash("The password reset link has expired.")
        return redirect(url_for("auth.login"))
    except BadSignature:
        flash("The password reset link is invalid ")
        return redirect(url_for("auth.login"))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        password = form.password.data
        user = Users.query.filter_by(email=email).first()
        user.generate_password_hash(password)
        db.session.commit()
        flash("Your password has been updated successfully")
        return redirect(url_for("auth.login"))

    return render_template("auth/confirmpassword.html", form=form, token=token)


@auth.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("auth.login"))


@auth.route("/admin", methods=["GET"])
@login_required
@check_confirmed
def admin():
    if current_user.is_admin != True:
        flash("You need to be an admin to access this page")
        return redirect(url_for("auth.login"))
    return render_template("dashboard/admin_dashboard.html")
