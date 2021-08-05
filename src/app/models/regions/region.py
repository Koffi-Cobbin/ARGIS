from database.db import db

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    towns = db.relationship("Town", lazy='select', backref=db.backref('region', lazy='joined'))