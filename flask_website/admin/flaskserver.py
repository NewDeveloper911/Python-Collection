from flask import Blueprint, render_template

todoapp = Blueprint("todoapp",  __name__, static_folder="static", template_folder="templates")

@todoapp.route('/')
def index():
    return render_template("todo_index.html")
