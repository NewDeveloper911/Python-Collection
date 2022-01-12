from flask import Flask, redirect, url_for, render_template,request, session, flash, g
from admin.blueprint import blueprint #this is possible because my empty __init__.py file allows me to access files from different folders
#import songify as song #This can be used to play songs currently downloaded on device
from flask_sqlalchemy import SQLAlchemy #import at shell using: pip install flask-sqlalchemy
from admin.flaskserver import todo
import logging
from flask_migrate import Migrate
from databases import db, users #This allows me to access databases in other files


app = Flask(__name__)

@app.before_request
def load_user():
    g.user = None

    if 'user' in session:
        user = users.query.filter_by(name=session['user']).first()
        g.user = session['user']


#Sets up my configuration files for my website to hide private information as well
if app.config['ENV'] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config['ENV'] == "development":
    app.config.from_object("config.DevelopmentConfig")
else:
    app.config.from_object("config.TestingConfig")

app.register_blueprint(blueprint, url_prefix="/admin")
app.register_blueprint(todo, url_prefix="/todo")

logging.basicConfig(level=logging.DEBUG)

'''
if the url prefix is as above, it will pass the rest ofthe url to my blueprint file 
'''
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.permanent_session_time = timedelta(hours=2)

#This will set up our website using the configuration settings from config.py

#db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    #print(app.config)
    app.logger.info(app.config) #I use this so I can see print messages while 
    #running my Flask file at the same time - not possible on Mac apparantly
    return render_template("flaskindex.html")
    #render_template just gets rid of complaints from flask
    app.logger.info(metadata.tables.keys())
@app.route("/<name>")
def homepage(name):
    return render_template("flaskindex.html", content=name)

@app.route("/view")
def view():
    return render_template("flaskindex.html",values=users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.pop('user', None)

        username = request.form['nm'] #searches for name submitted at login page
        found_user = users.query.filter_by(name=username).first() #checks to see if user exists in database

        #If error shows, that means for now that user doesn't exist
        app.logger.info(found_user.name) #prints to console during runtime (can't use print now)
        if found_user: #If existing user
            session['user'] = found_user.name #creates new session for user
            detail = session.get('user')
            app.logger.info(str(detail) + " - Hooray, we are logged in.")
            return redirect(url_for('user', detail=session['user'])) #redirects to user-only content
        
        flash("Unfortunately, we have an internal error at our servers. Either your account doesn't exist or we have a bug.")
        return redirect(url_for('login'))

    return render_template("login.html")

@app.route("/logout", methods=['POST', 'GET'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
    
@app.route("/user/<detail>", methods=['POST','GET'])
def user(detail):
    if request.method == "POST":
        email = request.form["email"]
        session["email"] = email

        found_user = users.query.filter_by(name=str(detail)).first()
        found_user.email = email

        db.session.commit()
        flash("Email has been saved successfully")
        app.logger.info("Your email, which is " + str(session.get('email')) + " has been saved successfully")
        return render_template("flaskindex.html", user=str(detail))
    else:
        if "email" in session:
            email = session["email"]
            app.logger.info("Email has been set firmly")
            return render_template("flaskindex.html", user=str(detail))
        if detail:
            return render_template("flaskindex.html", user=str(detail))
        else:
            app.logger.info("Tried to skip the queue, huh? Your mistake.")
            flash("You are not logged in yet, you should login in for full access to all features")
            return redirect(url_for("login"))           

if __name__ == "__main__":
    #db.create_all() #creates the database in case it doesn't already exist
    app.run(debug=True)
