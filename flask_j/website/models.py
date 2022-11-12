# database models
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # foreign key
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'))  # one-to-many relationship


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    notes = db.relationship('Note')
