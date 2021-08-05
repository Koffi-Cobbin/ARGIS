from src.database.db import db

class Polyline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    town_id = db.Column(db.Integer, db.ForeignKey(''), nullable=False)
    coordinates = db.Column(db.Integer, db.ForeignKey(''), nullable=True)
