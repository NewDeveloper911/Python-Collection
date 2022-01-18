from flask import Flask, redirect, url_for, render_template,request, session, flash, g
from admin.blueprint import blueprint #this is possible because my empty __init__.py file allows me to access files from different folders
#import songify as song #This can be used to play songs currently downloaded on device
from flask_sqlalchemy import SQLAlchemy #import at shell using: pip install flask-sqlalchemy
from admin.flaskserver import todo
import logging
from flask_migrate import Migrate
from databases import db, users #This allows me to access databases in other files
from werkzeug.security import generate_password_hash, check_password_hash

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

app.register_blueprint(blueprint, url_prefix="/education")
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

@app.route("/view")
def view():
    return render_template("flaskindex.html",values=users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.pop('user', None)

        username = request.form.get('nm')#searches for name submitted at login page
        password = request.form.get('password')
        found_user = users.query.filter_by(name=username).first() #checks to see if user exists in database

        try:
            #If error shows, that means for now that user doesn't exist
            app.logger.info(found_user.name) #prints to console during runtime (can't use print now)
        except:
            app.logger.warning(username + " doesn't exist on our database.")
            app.logger.warning(users.query.all())
        if found_user: #If existing user
            if check_password_hash(found_user.password, password):
                session['user'] = found_user.name #creates new session for user
                app.logger.info(str(session.get('user')) + " - Hooray, we are logged in.")
                return redirect(url_for('user', detail=session.get('user'), user=users.query.filter_by(name=session.get('user')).first())) #redirects to user-only content
            flash('Incorrect password entered. Please try again', category='error')
        return redirect(url_for('login'))
    else:
        if 'user' in session:
            app.logger.info("You are already logged in")
            return redirect(url_for('user', detail=session.get('user'))) #redirects to user-only content

    return render_template("login.html")

@app.route("/logout", methods=['POST', 'GET'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
    
@app.route("/user/<detail>", methods=['POST','GET'])
def user(detail):
        if request.method == "POST":
             return redirect(url_for('edit_profile', detail=detail))
        else:
            if detail == session.get('user'): 
                return render_template("flaskindex.html", detail=str(detail), user=users.query.filter_by(name=detail).first())
            else:
                app.logger.info("Tried to skip the queue, huh? Your mistake.")
                flash("You are not logged in yet, you should login in for full access to all features")
                return redirect(url_for("login"))

@app.route("/user/<detail>/edit_profile", methods=['POST','GET'])
def edit_profile(detail):
    if request.method == "POST":
        found_user = users.query.filter_by(name=str(detail)).first()
        email = request.form.get("email")
        if email:
            session["email"] = email
            found_user.email = email
            flash("Email has been saved successfully")
            app.logger.info("Your email, which is " + str(session.get('email')) + " has been saved successfully")

        name = request.form.get('nm')
        if name:
            session["user"] = name
            found_user.name = name
            flash("Name has been saved successfully")
            app.logger.info("Your name, which is " + str(users.query.filter_by(name=str(name)).first().name) + " has been saved successfully")

        about_me = request.form.get('about_me')
        if about_me:
            found_user.about_me = about_me
            flash("Your self-description has been saved successfully")
            app.logger.info(users.query.filter_by(about_me=about_me).first().about_me)

        p1 = request.form.get('password1')
        p2 = request.form.get('password2')
        if p1 and p2:
            if p1 == p2:
                found_user.password = p1
                flash("Password has been saved successfully", category='info')
                app.logger.info("Your password, which is " + str(users.query.filter_by(password=p1).first().name) + " has been saved successfully")

        db.session.commit()
        
        return render_template("flaskindex.html", detail=str(detail), user=users.query.filter_by(name=detail).first())
    else:
        if "email" in session:
            email = session["email"]
            app.logger.info("Email has been set firmly")
            return render_template("flaskindex.html", detail=str(detail), user=users.query.filter_by(name=detail).first())
        if detail:
            return render_template("flaskindex.html", detail=str(detail), user=users.query.filter_by(name=detail).first())
        else:
            app.logger.info("Tried to skip the queue, huh? Your mistake.")
            flash("You are not logged in yet, you should login in for full access to all features")
            return redirect(url_for("login"))

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('nm')
        email = request.form.get('email')
        p1 = request.form.get('password1')
        p2 = request.form.get('password2')
        if len(email) < 12 and "@" not in email and ".com" not in email:
            flash("Please input an email in the correct format, containing an @ and a '.com' ", category='warning')
        elif p1 != p2 or len(p1) == 0 or len(p2) == 0:
            flash("Please enter the same password in both password input boxes", category='warning')
        elif len(users.query.filter_by(name=name).all()) > 1 or len(users.query.filter_by(email=email).all()) > 1:
            flash("Perhaps you already have an account. Try logging in with that account, if you remember the details fully", category='warning')
            return redirect(url_for('login'))
        else:
            new_user = users(name=name, email=email, password=generate_password_hash(p1, "pbkdf2:sha512"))
            db.session.add(new_user)
            db.session.commit()
            try:  
                #session['user'] = users.query.filter_by(name=name).first().name
                #Seem to be unable to search the database
                return redirect(url_for('user', detail=name, user=users.query.filter_by(name=name).first()))
            except:
                app.logger.info("We have a problem, officer. {} is not bein put into the database".format(name))
                app.logger.info(session.get('user'))
                app.logger.info(users.query.all())
            
    return render_template('signup.html')

@app.route('/delete/<user>')
def delete(user):
    #return "<h1>{}</h1>".format(id)
    item = users.query.filter_by(name=user).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all(app=app) #creates the database in case it doesn't already exist
    app.run(debug=True)
