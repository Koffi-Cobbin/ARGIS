from database.db import db
from app.models.polylines import Polyline


class Polyline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    town_id = db.Column(db.Integer, db.ForeignKey(''), nullable=False)
    coordinates = db.Column(db.Integer, db.ForeignKey(''), nullable=True)
