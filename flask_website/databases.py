from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func
from .logs import *
from hashlib import md5

import sys
if sys.version_info >= (3, 0):
    enable_search = False
    error("We are unable to use whoosh_alchemy")
else:
    enable_search = True
    import flask_whooshalchemy as whooshalchemy

db = SQLAlchemy()

class users(db.Model, UserMixin):
    #__tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True) 
    name = db.Column("name", db.String(100), unique=True)
    about_me = db.Column("about_me", db.String(200))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    tasks = db.relationship('Todo', backref='post_author', lazy='dynamic')
    learn = db.relationship('Learning', backref='author', lazy='dynamic')
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
    '''
    For those unaware of SQL, I have set a column(field using the SQL jargon) called 
    'id' which will be my primary_key. The primary key is used to identify the 
    different types of records(rows) which each hold data about the different users.
     This means that the primary key has to be unique here for each of the users, 
     in order to find the right data. Each column can only hold data of a certain type,
      so I have used integers because it is simplest
    '''
    '''
    the number in the brackets next to db.String define the maximum length of the strings allowed within that colummn
    '''
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def __repr__(self):
        return '<Username: {0}, Email: {1}>'.format(self.name, self.email)
    pass

#This database handles all tasks set per user
class Todo(db.Model):
    #__tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    body= db.Column(db.String(300), nullable=False)
    author= db.Column(db.String(100), nullable=False) #I need to update my table somehow
    timestamp = db.Column(db.DateTime(timezone=True), index=True, default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    complete = db.Column(db.Boolean)

    #users_rel = db.relationship(users)
    def __repr__(self):
        return '<Task: {}>'.format(self.body)

    pass

class Learning(db.Model):
    #__searchable__ = ['title', 'body']
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(300), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=func.now())
    email = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __repr__(self):
        return '<Post title: {}>'.format(self.title)

    pass

if enable_search:
    whooshalchemy.whoosh_index(app, Learning)