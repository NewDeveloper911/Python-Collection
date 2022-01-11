from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import sys
import logging
from flask_sqlalchemy import SQLAlchemy
from .databases import db,users, Todo
from flask_login import login_required, current_user

todo = Blueprint("todo",  __name__, static_folder="static", template_folder="templates")

@todo.route('/')
@login_required
def todoindex():
    #todo_list = Todo.query.filter_by(complete=False, author=users.query.filter_by(name=current_user.name).first()).all() # Fetches all todos from my database
    #completed_todos = Todo.query.filter_by(complete=True, author=users.query.filter_by(name=current_user.name).first()).all() # Fetches all complete tasks

    todo_list = Todo.query.filter_by(complete=False, author=current_user.name).all() # Fetches all todos from my database
    completed_todos = Todo.query.filter_by(complete=True, author=current_user.name).all() # Fetches all complete tasks
    return render_template("todoindex.html", user=current_user, Completed=completed_todos, todo_list=todo_list)

@todo.route('/add', methods=['GET','POST'])
@login_required
def addtask():
    task = Todo(body=request.form['task'], author=current_user.name, complete=False, post_author=users.query.filter_by(name=current_user.name).first())
    #task = Todo(body=request.form['task'], complete=False)

    #Here, I search for an incomplete task which the user has set
    if len(request.form['task']) > 1:
        db.session.add(task)
        db.session.commit() #here, i add this task to my todo-list database
    else:
        flash("Your task is too short. PLease enter a valid task.")
    #After, I will reload page to show changes to to-do
    return redirect(url_for("todo.todoindex", user=current_user))

@todo.route('/complete/<id>')
@login_required
def complete(id):
    #return "<h1>{}</h1>".format(id)
    item = Todo.query.filter_by(id=int(id), author=current_user.name).first()
    item.complete = True
    db.session.commit()
    return redirect(url_for("todo.todoindex", user=current_user))

@todo.route('/incomplete/<id>')
@login_required
def incomplete(id):
    #return "<h1>{}</h1>".format(id)
    item = Todo.query.filter_by(id=int(id), author=current_user.name).first()
    item.complete = False
    db.session.commit()
    return redirect(url_for("todo.todoindex", user=current_user))

@todo.route('/delete/<id>')
@login_required
def delete(id):
    #return "<h1>{}</h1>".format(id)
    item = Todo.query.filter_by(id=int(id), author=current_user.name).first()

    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("todo.todoindex", user=current_user))
