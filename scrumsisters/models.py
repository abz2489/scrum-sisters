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

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self


class Clubs(db.Model):
    """
    Clubs schema
    """
    id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self


class Age(db.Model):
    """
    Age schema
    """
    id = db.Column(db.Integer, primary_key=True)
    age_group = db.Column(db.String, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self


class Training(db.Model):
    """
    Training Days schema
    """
    id = db.Column(db.Integer, primary_key=True)
    training_day = db.Column(db.String, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self


class Teams(db.Model):
    """
    Teams schema
    """
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(150), nullable=False)
    training_time = db.Column(db.Time, nullable=False)
    training_location = db.Column(db.Text, nullable=False)
    fb_url = db.Column(db.Text, nullable=True)
    tiktok_url = db.Column(db.Text, nullable=True)
    insta_url = db.Column(db.Text, nullable=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self