from flask import render_template, flash
from forms import UserRegistrationForm
from sqlalchemy import text
from scrumsisters import app, db, migrate
from scrumsisters.models import Users, Clubs, Age, Days, Teams, clubs_list
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    first_name = None
    last_name = None
    email = None
    form = UserRegistrationForm()
    # form validation
    if form.validate_on_submit():
        first_name = form.first_name.data
        form.first_name.data = ''
        last_name = form.last_name.data
        form.last_name.data = ''
        email = form.email.data
        form.email.data = ''
    return render_template(
        "register.html",
        first_name=first_name,
        last_name=last_name,
        email=email,
        form=form
        )
