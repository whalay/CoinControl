import email_validator
from flask_jwt_extended import current_user
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    FloatField,
    IntegerField,
    PasswordField,
    StringField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Regexp,
    ValidationError,
)

from coincontrol.models import Budgets, Users


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=25)]
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            Length(min=6, max=35, message="Little short for an email address?"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            EqualTo("confirm_password", message="Password must match confirm password"),
            Length(min=5, max=50, message="Password is too short"),
            Regexp(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&\#])[A-Za-z\d@$!%*?&\#]+$",
                message="Password must include at least one uppercase letter, one lowercase letter, one number, and one special character",
            ),
        ],
    )
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Sign up")

    def validate_username(self, username):
        print(username.data)
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username is already in use by another user")

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email is taken. Please choose a different one")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            Length(min=6, max=35, message="Little short for an email address?"),
        ],
    )
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            EqualTo("confirm_password", message="Password must match confirm password"),
            Length(min=5, max=50, message="Password is too short"),
            Regexp(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&\#])[A-Za-z\d@$!%*?&\#]+$",
                message="Password must include at least one uppercase letter, one lowercase letter, one number, and one special character",
            ),
        ],
    )
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Reset password")

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                "There is no account with that email. You must register first."
            )


class EditProfileForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=25)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username is already in use by another user")

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                "There is no account with that email. You must register first."
            )


class EmailForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Send")

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                "There is no account with that email. You must register first."
            )


class IncomeForm(FlaskForm):
    amount = FloatField("Amount", validators=[DataRequired()])


class BudgetForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    amount = FloatField("Amount", validators=[DataRequired()])

    def validate_name(self, name):
        name = name.data.replace(" ", "-")
        budget = Budgets.query.filter_by(name=name).first()
        if budget:
            raise ValidationError("Budget name already exists")


class ExpenseForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    amount = FloatField("Amount", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    account_number = StringField(
        "Account Number",
        validators=[
            DataRequired(),
            Length(
                min=10,
                max=10,
                message="Invalid account number field, Please enter 10-digit account number",
            ),
        ],
    )
    bank_name = StringField("Bank Name", validators=[DataRequired()])

    def validate_name(self, name):
        budget = Budgets.query.filter_by(
            user_id=current_user.user_id, name=name.data
        ).first()
        if budget is None:
            raise ValidationError("Budget name does not exist")

    def validate_amount(self, amount):
        budget = Budgets.query.filter_by(
            user_id=current_user.user_id, name=self.name.data
        ).first()
        if not budget:
            raise ValidationError("Budget not found")
        if amount.data > budget.amount:
            raise ValidationError("Insufficient Budget funds, Please top up")
