from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import logging
from .databases import db, users, Todo, Learning
import flask_website.config as config

from whoosh.filedb.filestore import FileStorage
from whoosh.fields import Schema, TEXT, ID

DB_NAME = "users.sqlite3"

def create_app():
    app = Flask(__name__)

    #Sets up my configuration files for my website to hide private information as well
    if app.config['ENV'] == "production":
        app.config.from_object(config.ProductionConfig)
    elif app.config['ENV'] == "development":
        app.config.from_object(config.DevelopmentConfig)
    else:
        app.config.from_object(config.TestingConfig)

    db.init_app(app)

    from flask_website.admin.education import blueprint
    from .admin.flaskserver import todo
    from .admin.home import home

    app.register_blueprint(blueprint, url_prefix="/learning")
    app.register_blueprint(todo, url_prefix="/todo")
    app.register_blueprint(home, url_prefix="/")

    logging.basicConfig(level=logging.DEBUG)


    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'home.login'
    login_manager.login_message = 'You must login or sign up to gain access to this page'
    login_manager.refresh_view = "home.login"
    login_manager.needs_refresh_message = (
        u"To protect your account, please reauthenticate to access this page."
    )
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return users.query.get(int(id))

    #Search-only section
    """
    search_is_new = False
    if not os.path.exists(WHOOSH_BASE):
        os.mkdir(WHOOSH_BASE)
        search_is_new = True
    search_storage = FileStorage(WHOOSH_BASE)
    search_ix = None
    if search_is_new:
        schema = Schema(id=ID(stored=True), body=TEXT())
        search_ix = search_storage.create_index(schema)
    else:
        search_ix = search_storage.open_index()
    """
    return app


def create_database(app):
    if not path.exists('flask_website/admin/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')