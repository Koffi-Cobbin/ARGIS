from database.db import db

class Town(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id', use_alter=True), nullable=False)
    polylines = db.relationship("Polyline", lazy='select', backref=db.backref('town', lazy='joined'))
