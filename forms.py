from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    EmailField,
    SelectField,
    SubmitField
    )
from wtforms.validators import DataRequired, EqualTo


# User registration form class
class UserRegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    club = SelectField("Clubs", coerce=int)
    user_password = PasswordField(
        'Password', validators=[DataRequired(), EqualTo(
            'confirm_password', message="Passwords do not match!")])
    confirm_password = PasswordField(
        'Confirm_password', validators=[DataRequired()])
    submit = SubmitField("Submit")


# User sign in form class
class UserSignInForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")
