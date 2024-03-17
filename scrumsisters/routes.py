from flask import render_template, flash, redirect, url_for
from markupsafe import Markup
from forms import UserRegistrationForm, UserSignInForm, AddTeamForm
from sqlalchemy import text
from scrumsisters import app, db, migrate
from scrumsisters.models import Users, Clubs, Age, Days, Teams
from scrumsisters.models import generate_password_hash, check_password_hash
from scrumsisters import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    logout_user,
    current_user,
    login_manager
)


@app.route("/")
def home():
    teams = Teams.query.all()
    return render_template("index.html", teams=teams)


@app.route("/teams")
def teams():
    teams = Teams.query.all()
    return render_template("teams.html", teams=teams)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserRegistrationForm()
    first_name = None
    last_name = None
    email = None
    user_password = None
    club = [(club.id, club.club_name) for club in Clubs.query.all()]
    form.club.choices = club
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
                user_password=password_hash,
                club_id=form.club.data,
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
def login():
    form = UserSignInForm()
    # Validate log in details
    if form.validate_on_submit():
        # Check if user email exists already
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            # Check password hash
            if check_password_hash(user.user_password, form.password.data):
                login_user(user)
                return redirect(url_for('user_profile'))
            else:
                flash("Wrong email or password")
        else:
            flash(Markup("User doesn't exist, \
            try again or <a href='/register'>register</a> for an account"))
    return render_template("signin.html", form=form)


@app.route("/signout", methods=["GET", "POST"])
@login_required
def user_signout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/profile")
@login_required
def user_profile():
    return render_template('profile.html')


@app.route("/edit_user_profile/<user_id>", methods=["GET", "POST"])
@login_required
def edit_user_profile(user_id):
    user_id = Users.query.get_or_404(user_id)
    form = UserRegistrationForm()
    club = [(club.id, club.club_name) for club in Clubs.query.all()]
    form.club.choices = club
    if form.validate_on_submit():
        # Hash password
        password_hash = generate_password_hash(
            form.user_password.data, method="scrypt")
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        current_user.user_password = password_hash
        current_user.club_id = form.club.data
        db.session.add(user_id)
        db.session.commit()
        flash("User Details Changed Successfully!")
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.email.data = current_user.email
    form.club.data = current_user.club_id
    return render_template('edit_user_profile.html', form=form)


@app.route("/delete_user/<user_id>")
@login_required
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("User Account Deleted Successfully!")
    return redirect(url_for('register'))


@app.route("/club_page/<club_id>")
@login_required
def club_page(club_id):
    club = Clubs.query.get_or_404(club_id)
    return render_template('club_page.html')


@app.route("/add_team/<user_club_id>", methods=["GET", "POST"])
@login_required
def add_team(user_club_id):
    form = AddTeamForm()
    club = [(club.id, club.club_name) for club in Clubs.query.all()]
    age_group = [(group.id, group.age_group) for group in Age.query.all()]
    training_day1 = [(day.id, day.day) for day in Days.query.all()]
    training_day2 = [(day.id, day.day) for day in Days.query.all()]
    form.club.choices = club
    form.age_group.choices = age_group
    form.training_day1.choices = training_day1
    form.training_day2.choices = training_day2
    form.club.data = current_user.club_id
    form.user_id.data = current_user.id
    # form validation
    if form.validate_on_submit():
        # Check if team name exists already
        team = Teams.query.filter_by(team_name=form.team_name.data).first()
        if team:
            flash("Team already exists")
            return redirect(url_for("add_team"))
        if team is None:
            team = Teams(
                team_name=form.team_name.data,
                club_id=form.club.data,
                age_group_id=form.age_group.data,
                training_day1=form.training_day1.data,
                training_day2=form.training_day2.data,
                training_time=form.training_time.data,
                training_location=form.training_location.data,
                fb_url=form.fb_url.data,
                tiktok_url=form.tiktok_url.data,
                insta_url=form.insta_url.data,
                users_id=form.user_id.data
            )
            db.session.add(team)
            db.session.commit()
    return render_template('add_team.html', form=form)


@app.route("/team_profile/<team_club>")
@login_required
def team_profile(team_club):
    team = Teams.query.get_or_404(team_club)
    return render_template('team_profile.html')


@app.route("/edit_team_profile/<team_id>", methods=["GET", "POST"])
@login_required
def edit_team_profile(team_id):
    team = Teams.query.get_or_404(team_id)
    form = AddTeamForm()
    club = [(club.id, club.club_name) for club in Clubs.query.all()]
    age_group = [(group.id, group.age_group) for group in Age.query.all()]
    training_day1 = [(day.id, day.day) for day in Days.query.all()]
    training_day2 = [(day.id, day.day) for day in Days.query.all()]
    form.club.choices = club
    form.age_group.choices = age_group
    form.training_day1.choices = training_day1
    form.training_day2.choices = training_day2
    form.club.data = current_user.club_id
    form.user_id.data = current_user.id

    if form.validate_on_submit():
        team.team_name = form.team_name.data
        team.club_id = form.club.data
        team.age_group_id = form.age_group.data
        team.training_day1 = form.training_day1.data
        team.training_day2 = form.training_day2.data
        team.training_time = form.training_time.data
        team.training_location = form.training_location.data
        team.fb_url = form.fb_url.data
        team.tiktok_url = form.tiktok_url.data
        team.insta_url = form.insta_url.data
        db.session.add(team)
        db.session.commit()
        flash("Team Details Changed Successfully!")

    form.team_name.data = team.team_name
    form.club.data = team.club_id
    form.age_group.data = team.age_group_id
    form.training_day1.data = team.training_day1
    form.training_day2.data = team.training_day2
    form.training_time.data = team.training_time
    form.training_location.data = team.training_location
    form.fb_url.data = team.fb_url
    form.tiktok_url.data = team.tiktok_url
    form.insta_url.data = team.insta_url
    return render_template('edit_team_profile.html', form=form, team=team)


@app.route("/delete_team/<team_id>")
@login_required
def delete_team(team_id):
    team = Teams.query.get_or_404(team_id)
    db.session.delete(team)
    db.session.commit()
    return redirect(url_for('club_page', club_id=current_user.club_id))
