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
        return self


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
        return self


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
        return self


class Training(db.Model):
    """
    Training Days schema
    """
    id = db.Column(db.Integer, primary_key=True)
    training_day = db.Column(db.String, nullable=False)

    # relationships
    teams = db.relationship("Teams", backref="training", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self


class Teams(db.Model):
    """
    Teams schema
    """
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(150), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.id"), nullable=False)
    age_group_id = db.Column(
        db.Integer, db.ForeignKey("age.id"), nullable=False)
    training_id = db.Column(db.Integer, db.ForeignKey(
        "training.id"), nullable=False)
    training_time = db.Column(db.Time, nullable=False)
    training_location = db.Column(db.Text, nullable=False)
    fb_url = db.Column(db.Text, nullable=True)
    tiktok_url = db.Column(db.Text, nullable=True)
    insta_url = db.Column(db.Text, nullable=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self
