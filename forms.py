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


# Create a Form Class
class UserRegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    club = SelectField("Club", choices=[])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
            'confirm_password', message="Passwords do not match!")])
    confirm_password = PasswordField(
        'confirm_password', validators=[DataRequired()])
    submit = SubmitField("Submit")
