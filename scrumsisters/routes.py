from flask import render_template, flash, redirect, url_for
from forms import UserRegistrationForm, UserSignInForm
from sqlalchemy import text
from scrumsisters import app, db, migrate
from scrumsisters.models import Users, Clubs, Age, Days, Teams
from scrumsisters.models import generate_password_hash, check_password_hash
from scrumsisters import login_manager, login_user, login_required, logout_user


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
        if user:
            flash("Email already registered")
            return redirect(url_for("register"))
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
        flash("Registration Successful!")
        first_name = form.first_name.data
    return render_template(
        "register.html",
        first_name=first_name,
        last_name=last_name,
        email=email,
        password_hash=user_password,
        form=form
        )


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route("/signin", methods=["GET", "POST"])
def user_signin():
    form = UserSignInForm()
    # Validate log in details
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            # Check password hash
            if check_password_hash(user.user_password, form.password.data):
                login_user(user)
                return redirect(url_for('user_profile'))
            else:
                flash("Wrong email or password")
        else:
            flash("User doesn't exist, try again or register for an account")
    return render_template("signin.html", form=form)


@app.route("/signout", methods=["GET", "POST"])
@login_required
def user_signout():
    logout_user()
    return redirect(url_for('user_signin'))


@app.route("/profile")
@login_required
def user_profile():
    return render_template('profile.html')
