from scrumsisters import db


class Users(db.Model):
    """
    Users schema
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    confirm_password = db.Column(db.String(50), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.id"), nullable=False)

    # relationships
    teams = db.relationship("Teams", backref="users", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.first_name


class Clubs(db.Model):
    """
    Clubs schema
    """
    id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String(150), nullable=False)

    # relationships
    users = db.relationship("Users", backref="clubs", lazy=True)
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
    teams = db.relationship("Teams", backref="days", lazy=True)

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
    days_id = db.Column(db.Integer, db.ForeignKey(
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
