from flask_login import UserMixin
from . import db

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(100),unique=True)

class Entitymaster(db.Model,UserMixin):
    entityid = db.Column(db.Integer)
    entitytype = db.Column(db.String(100))
    entityname = db.Column(db.String(100))
    branchid = db.Column(db.Integer,primary_key=True)
    branchtype = db.Column(db.String(100))
    province = db.Column(db.String(100))
    city = db.Column(db.String(100))
    area = db.Column(db.String(100))
    branchcoordinates = db.Column(db.String(100))
    branchcontact = db.Column(db.String(100),unique=True)