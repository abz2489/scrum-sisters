from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    EmailField,
    SelectField,
    SelectMultipleField,
    SubmitField
    )
from wtforms.validators import DataRequired, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField
# from scrumsisters.models import clubs_list


# Create a Form Class
class UserRegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    user_password = PasswordField(
        'Password', validators=[DataRequired(), EqualTo(
            'confirm_password', message="Passwords do not match!")])
    confirm_password = PasswordField(
        'Confirm_password', validators=[DataRequired()])
    submit = SubmitField("Submit")
