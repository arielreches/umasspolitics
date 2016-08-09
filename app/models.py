from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    deviceid = db.Column(db.Integer)
    year = db.Column(db.String)
    home_location = db.Column(db.String)
    housing = db.Column(db.String)
    building = db.Column(db.String)
    candidate = db.Column(db.String)

    def __repr__(self):
        return 'Year ' + self.year