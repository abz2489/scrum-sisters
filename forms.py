from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    EmailField,
    SelectField,
    SubmitField,
    URLField,
    TimeField
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


# Add team form class
class AddTeamForm(FlaskForm):
    team_name = StringField("First Name", validators=[DataRequired()])
    club = SelectField("Club", coerce=int)
    age_group = SelectField("Age Group", coerce=int)
    training_days = SelectField("Training Days", coerce=int)
    training_time = TimeField('Training Time', validators=[DataRequired()])
    training_location = TextField(
        'Training Location', validators=[DataRequired()])
    fb_url = URLField("Facebook URL")
    tiktok_url = URLField("TikTok URL")
    insta_url = URLField("TikTok URL")
    submit = SubmitField("Submit")
