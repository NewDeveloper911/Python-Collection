from flask import Blueprint, render_template, request, redirect, url_for
import sys
import logging
from flask_sqlalchemy import SQLAlchemy
from databases import db, Todo

todo = Blueprint("todo",  __name__, static_folder="admin.static", template_folder="templates")
#database = current_app.config['SQLALCHEMY_DATABASE_URI']

@todo.route('/')
def todoindex():
    todo_list = Todo.query.filter_by(complete=False).all() # Fetches all todos from my database
    completed_todos = Todo.query.filter_by(complete=True).all() # Fectches all complete tasks
    return render_template("todoindex.html", todo_list=todo_list, completed_todos=completed_todos)

@todo.route('/add', methods=['GET','POST'])
def addtask():
    task = Todo(body=request.form['task'], complete=False)
    #Here, I search for an incomplete task which the user has set
    db.session.add(task)
    db.session.commit() #here, i add this task to my todo-list database
    #After, I will reload page to show changes to to-do
    return redirect(url_for("todo.todoindex"))

@todo.route('/complete/<id>')
def complete(id):
    #return "<h1>{}</h1>".format(id)
    item = Todo.query.filter_by(id=int(id)).first()
    item.complete = True
    db.session.commit()
    return redirect(url_for("todo.todoindex"))

@todo.route('/incomplete/<id>')
def incomplete(id):
    #return "<h1>{}</h1>".format(id)
    item = Todo.query.filter_by(id=int(id)).first()
    item.complete = False
    db.session.commit()
    return redirect(url_for("todo.todoindex"))

@todo.route('/delete/<id>')
def delete(id):
    #return "<h1>{}</h1>".format(id)
    item = Todo.query.filter_by(id=int(id)).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("todo.todoindex"))
