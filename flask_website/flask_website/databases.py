from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta, datetime

db = SQLAlchemy()

class users(db.Model):
    #__tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True) 
    '''
    For those unaware of SQL, I have set a column(field using the SQL jargon) called 
    'id' which will be my primary_key. The primary key is used to identify the 
    different types of records(rows) which each hold data about the different users.
     This means that the primary key has to be unique here for each of the users, 
     in order to find the right data. Each column can only hold data of a certain type,
      so I have used integers because it is simplest
    '''
    name = db.Column("name", db.String(100))
    email = db.Column(db.String(100))
    '''
    the number in the brackets next to db.String define the maximum length of the strings allowed within that colummn
    '''
    tasks = db.relationship('Todo', backref='author', lazy='dynamic')
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    pass

#This database handles all tasks set per user
class Todo(db.Model):
    #__tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    body= db.Column(db.String(300))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    complete = db.Column(db.Boolean)

    pass