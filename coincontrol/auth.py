from flask import Blueprint
from flask import request, render_template, redirect, url_for, flash
from coincontrol.forms import RegistrationForm, LoginForm, ResetPasswordForm, EmailForm
from coincontrol.extensions import bcrypt
from coincontrol.models import Users
from coincontrol.extensions import db
from flask_login import login_required, login_user, logout_user, current_user
from coincontrol.token import generate_confirmation_token, check_confirm_token
from datetime import datetime
from coincontrol.email import send_email
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
        subject = "CoinControl Email Confirmation"
        text = """\
            Thank you for registering with CoinControl
            """
        html = f"""\
            <html>
            <body>
                <h3>Dear {user.username},</h3><br>
                <p>Thank you for registering with CoinControl. To complete the registration process and activate your account, 
                we kindly ask you to confirm your email address by clicking on the link below:</p><br>
                <p><a href="{ confirm_url }">{ confirm_url }</a></p><br>
                <p>By clicking on the link, you will be directed to a confirmation page where you can verify your email address. 
                Please ensure that you complete this step to gain full access to our services.</p><br>
                <p>If you did not initiate this registration or believe this email was sent to you in error, please disregard it.</p><br>
                <p>If you have any questions or need further assistance, please do not hesitate to contact our support team at <a href="mailto:support@coincontrol.com">support@coincontrol.com</a>.</p><br>
                <p>Thank you for choosing Coincontrol. We look forward to serving you.</p><br>
                <p>Best regards,<br>
                Coincontrol Team.
                </p>
                </body>
            </html>
            """

        send_email(email, subject, text, html)

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
        flash("You have verified your account, you can now login to your dashboard. Thanks!")
    return redirect(url_for("main.home"))


@auth.route("/resend-token", methods=["GET"])
@login_required
def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for("auth.confirm_token", token=token, _external=True)
    subject = "CoinControl Resend Email Confirmation"
    text = """\
        Thank you for registering with CoinControl
        """
    html = f"""\
            <html>
            <body>
                <h3>Dear {current_user.username},</h3><br>
                <p>Thank you for registering with CoinControl. To complete the registration process and activate your account, 
                we kindly ask you to confirm your email address by clicking on the link below:</p><br>
                <p><a href="{ confirm_url }">{ confirm_url }</a></p><br>
                <p>By clicking on the link, you will be directed to a confirmation page where you can verify your email address. 
                Please ensure that you complete this step to gain full access to our services.</p><br>
                <p>If you did not initiate this registration or believe this email was sent to you in error, please disregard it.</p><br>
                <p>If you have any questions or need further assistance, please do not hesitate to contact our support team at <a href="mailto:support@coincontrol.com">support@coincontrol.com</a>.</p><br>
                <p>Thank you for choosing Coincontrol. We look forward to serving you.</p><br>
                <p>Best regards,<br>
                Coincontrol Team.
                </p>
                </body>
            </html>
            """

    send_email(current_user.email, subject, text, html)
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
        subject = "CoinControl Account Recovery"
        text = """\
            Follow the instructions bellow
            """
        html = f"""\
            <html>
            <body>
                <h3>Dear {user.username}</h3><br>
                <p>We have received your request for coin control recovery. 
                We understand that you are experiencing issues accessing your coins and we are here to assist you. 
                Please click the link below to initiate the recovery process</p><br>
                <p><a href="{ confirm_url }">{ confirm_url }</a></p><br>
                <p>If you have any questions or need further assistance, please do not hesitate to contact our support team at <a href="mailto:support@coincontrol.com">support@coincontrol.com</a>.</p><br>
                <p>Thank you for your patience and cooperation.</p><br>
                <p>Best regards,<br>
                Coincontrol Team.
                </p>
                </body>
            </html>
            """

        send_email(form_email, subject, text, html)
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
