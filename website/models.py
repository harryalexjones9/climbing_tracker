from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    fullName = db.Column(db.String(150))
    notes = db.relationship('Note')
    climbs = db.relationship('Climb')

class Climb(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    v0 = db.Column(db.Integer)
    v1 = db.Column(db.Integer)
    v2 = db.Column(db.Integer)
    v3 = db.Column(db.Integer)
    v4 = db.Column(db.Integer)
    v5 = db.Column(db.Integer)
    v6 = db.Column(db.Integer)
    v7 = db.Column(db.Integer)
    v8 = db.Column(db.Integer)
    v9 = db.Column(db.Integer)
    v10 = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))