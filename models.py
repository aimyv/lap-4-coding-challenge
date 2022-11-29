from . import db


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_path = db.Column(db.Text, nullable=False, unique=True)
    short_path = db.Column(db.String(50), unique=True)
