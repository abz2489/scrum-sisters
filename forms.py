from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    EmailField,
    SelectField,
    SelectMultipleField,
    SubmitField,
    URLField,
    TimeField,
    )
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Optional,
    URL,
    InputRequired
    )


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
    team_name = StringField("Team Name", validators=[DataRequired()])
    club = SelectField("Club", coerce=int)
    age_group = SelectField("Age Group", coerce=int)
    training_days = SelectMultipleField(
        "Training Days", coerce=int, validators=[InputRequired()])
    training_time = StringField('Training Time', validators=[DataRequired()])
    training_location = StringField(
        'Training Location', validators=[DataRequired()])
    fb_url = URLField(
        "Facebook URL", validators=[
            Optional(),
            URL(require_tld=False, message="Valid URL required!")])
    tiktok_url = URLField(
        "TikTok URL", validators=[
            Optional(),
            URL(require_tld=False, message="Valid URL required!")])
    insta_url = URLField(
        "Instagram URL", validators=[
            Optional(),
            URL(require_tld=False, message="Valid URL required!")])
    user_id = StringField("User", validators=[DataRequired()])
    submit = SubmitField("Submit")
