from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Role(db.model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    
    def __repr(self):
        return '<Role %r>' % self.name
    
    users = db.relationship('User', backref='role')
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    
    def __repr(self):
        return '<Role %r>' % self.name
    
    role_id = db.Column(db.integer, db.ForeignKey('roles.id0'))