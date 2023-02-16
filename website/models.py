from flask_login import UserMixin
from . import db


class studentii(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    prenume = db.Column(db.String(255), nullable=False)
    nume = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    parola = db.Column(db.String(255), nullable=False)
    facultate = db.Column(db.String(255), nullable=False)
    anul = db.Column(db.String(255), nullable=False)
