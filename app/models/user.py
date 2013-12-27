from app import db
from roles import roles as ROLE


class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    secondary_email = db.Column(db.String(120))
    mobile = db.Column(db.Integer)
    secondary_mobile = db.Column(db.Integer)
    facebook_id = db.Column(db.Integer, unique=True)
    google_id = db.Column(db.Integer, unique=True)
    linkedin_id = db.Column(db.Integer, unique=True)
    gender = db.Column(db.String(6))
    city = db.Column(db.String(100))
    city_lat_long = db.Column(db.String(150))
    salt = db.Column(db.String(64))
    hash = db.Column(db.String(64))
    ref_by = db.Column(db.String(32))
    ref_link = db.Column(db.String(32))
    status = db.Column(db.Integer)
    primary_role = db.Column(db.String(20), default=ROLE.NORMAL)
    seconday_role = db.Column(db.String(20))
    last_login = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, first_name=None,
                 last_name=None, email=None,
                 username=None, salt=None,
                 hash=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.salt = salt
        self.hash = hash

    def getStatus(self):
        return ROLE.STATUS[self.status]

    def getPrimaryRole(self):
        return ROLE.ROLE[self.primary_role]

    def getSecondaryRole(self):
        return ROLE.ROLE[self.seconday_role]

    def __repr__(self):
        return '<User %r>' % (self.name)
