from scrumsisters import db
from scrumsisters import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model, UserMixin):
    """
    Users schema
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.id"), nullable=False)

    # Hashed passwords
    user_password = db.Column(db.String(200))

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute!")

    @password.setter
    def password(self, password):
        self.user_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.user_password, password)

    # relationships
    teams = db.relationship("Teams", backref="users", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return '<Name %r>' % self.first_name


class Clubs(db.Model):
    """
    Clubs schema
    """
    id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String(150), nullable=False)

    # relationships
    users = db.relationship("Users", backref="clubs", uselist=False)
    teams = db.relationship(
        "Teams",
        backref="clubs",
        cascade="all, delete",
        lazy=True
        )

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.club_name


class Age(db.Model):
    """
    Age schema
    """
    id = db.Column(db.Integer, primary_key=True)
    age_group = db.Column(db.String, nullable=False)

    # relationships
    teams = db.relationship("Teams", backref="age", uselist=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.age_group


class Days(db.Model):
    """
    Training Days schema
    """
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String, nullable=False)

    # relationships
    teams = db.relationship(
        "Teams",
        primaryjoin="Days.id==Teams.training_day1",
        backref="days",
        lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.day


class Teams(db.Model):
    """
    Teams schema
    """
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(150), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.id"), nullable=False)
    age_group_id = db.Column(
        db.Integer, db.ForeignKey("age.id"), nullable=False)
    training_day1 = db.Column(db.Integer, db.ForeignKey(
        "days.id"), nullable=False)
    training_day2 = db.Column(db.Integer, db.ForeignKey(
        "days.id"), nullable=False)
    training_time = db.Column(db.Time, nullable=False)
    training_location = db.Column(db.Text, nullable=False)
    fb_url = db.Column(db.Text, nullable=True)
    tiktok_url = db.Column(db.Text, nullable=True)
    insta_url = db.Column(db.Text, nullable=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.team_name
