from hello import app, db
from admin.databases import users, Todo, Learning

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': users, 'Todo': Todo, 'Learning': Learning}