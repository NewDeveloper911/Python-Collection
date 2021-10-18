from datetime import timedelta
import os

'''
This file controls the variables for any configurations in Flask that I may want to use
later on in the development of the website
'''
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.urandom(16)
    DB_NAME = "database"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    UPLOADS = "/Users/mac/MacPython/Hacktoberfest2020/Python-Collection/flask_website/admin/static/Images"

    SESSION_COOKIE_SECURE = True #Cookies are transferred if connected to HTTPS 

    SESSION_COOKIE_SAMESITE="Lax"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///admin/users.sqlite3'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PERMANENT_SESSION_TIME = timedelta(hours=3)

    WHOOSH_BASE = os.path.join(basedir, 'users.sqlite3')

    MAX_SEARCH_RESULTS = 50

class ProductionConfig(Config):
    #Inherits all data and attributes of config class
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    #Sets debugging to true to enable reload of server

    DB_NAME = "todo"
    DB_USERNAME = "todouser"
    DB_PASSWORD = "flask"

    UPLOADS = "/Users/mac/MacPython/Hacktoberfest2020/Python-Collection/flask_website/admin/templates"

class TestingConfig(Config):
    TESTING = True
    #Allows the user to test functionality

    DB_NAME = "testing"
    DB_USERNAME = "example"
    DB_PASSWORD = "test"

    UPLOADS = "/Users/mac/MacPython/Hacktoberfest2020/Python-Collection/flask_website/flaskenv/development"

    SESSION_COOKIE_SECURE = False

    PERMANENT_SESSION_TIME = timedelta(minutes=55)