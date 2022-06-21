from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func
from hashlib import md5
from flask import Flask

db = SQLAlchemy()

class users(db.Model, UserMixin):
    #__tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True) 
    name = db.Column("name", db.String(100), unique=True)
    about_me = db.Column("about_me", db.String(200))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    tasks = db.relationship('Todo', backref='post_author', lazy='dynamic')
    learn = db.relationship('Learning', backref='question_author', lazy='dynamic')
    reply = db.relationship('Replies', backref='comment_author', lazy='dynamic')
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
        return '<Username: {0}, About me: {1}>'.format(self.name, self.about_me)
    pass

#This database handles all tasks set per user
class Todo(db.Model):
    #__tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    body= db.Column(db.String(300), nullable=False)
    author= db.Column(db.String(30), nullable=False) #I need to update my table somehow
    timestamp = db.Column(db.DateTime(timezone=True), index=True, default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    complete = db.Column(db.Boolean)

    #users_rel = db.relationship(users)
    def __repr__(self):
        return '<Task: {}>'.format(self.body)

    pass

'''
#Intermediate table between Learning posts and Tag table, to ensure 2NF
'''
association_table = db.Table(
    'association',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('learning_id', db.Integer, db.ForeignKey('learning.id'))
)

class Tag(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey('learning.id'), primary_key=True)
    author = db.relationship('Learning',secondary=association_table,backref='post_tags')

    def __repr__(self):
        return '<Tag name: {}>'.format(self.name)

class Learning(db.Model):
    #__searchable__ = ['title', 'body']
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(300), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=func.now())
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)
    last_modified = db.Column(db.DateTime, index=True, default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    replies = db.relationship('Replies', backref='post')
    
    def __repr__(self):
        return '<Post title: {}>'.format(self.title)

    pass

'''
#Intermediate table between Learning posts and Replies table, to ensure 2NF
'''
comment_table = db.Table(
    'comment',
    db.Column('reply_id', db.Integer, db.ForeignKey('replies.id')),
    db.Column('learning_id', db.Integer, db.ForeignKey('learning.id'))
)

class Replies(db.Model):
    #__searchable__ = ['title', 'body']
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    reply = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=func.now())
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)
    last_modified = db.Column(db.DateTime, index=True, default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('learning.id'), primary_key=True)
    author = db.relationship('Learning',secondary=comment_table,backref='post_replies')
    
    def __repr__(self):
        return '<Post title: {}>'.format(self.title)

    pass