from flask import render_template, flash
from forms import UserRegistrationForm
from sqlalchemy import text
from scrumsisters import app, db, migrate
from scrumsisters.models import Users, Clubs, Age, Days, Teams
from scrumsisters.models import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    first_name = None
    last_name = None
    email = None
    user_password = None
    form = UserRegistrationForm()
    # form validation
    if form.validate_on_submit():
        # Check if user email exists already
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            # Hash password
            password_hash = generate_password_hash(
                form.user_password.data, method="scrypt")
            user = Users(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                user_password=password_hash
            )
            db.session.add(user)
            db.session.commit()
        first_name = form.first_name.data
    return render_template(
        "register.html",
        first_name=first_name,
        last_name=last_name,
        email=email,
        password_hash=user_password,
        form=form
        )
