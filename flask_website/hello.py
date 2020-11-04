from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from admin.blueprint import blueprint, todoapp #this is possible because my empty __init__.py file allows me to access files from different folders
import pyserver as song
from flask_sqlalchemy import SQLAlchemy #import at shell using: pip install flask-sqlalchemy

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix="/admin")
app.redgister_blueprint(todoapp, url_prefix="/todo")
'''
if the url prefix is as above, it will pass the rest ofthe url to my blueprint file 
'''
app.secret_key = "bro"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_time = timedelta(hours=2)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True) 
    '''
    For those unaware of SQL, I have set a column(field using the SQL jargon) called 'id' which will be my primary_key. The primary key is used to identify the different types of records(rows) which each hold data about the different users. This means that the primary key has to be unique here for each of the users, in order to find the right data. Each column can only hold data of a certain type, so I have used integers because it is simplest
    '''
    name = db.Column("name", db.String(100))
    email = db.Column(db.String(100))
    '''
    the number in the brackets next to db.String define the maximum length of the strings allowed within that colummn
    '''
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
@app.route("/<name>")
def homepage(name):
    return render_template("flaskindex.html", content=name)

@app.route("/view")
def view():
    return render_template("flaskindex.html",values=users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST": #POST is used to add information; GET is used to get information
        session.permanent = True #whether my data will remian after i come off the website
        user = request.form["nm"] #gets the data from the 'nm' key in a dictionary
        session["user"] = user #a session is made for the user which is logged in
        found_user = users.query.filter_by(name=user).first() #how we will check for users in the database
        if found_user:
            session["email"] = found_user.email
            session["user"] = found_user.name
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit() #commits change to databse. like git
            
        flash("Login successful!") #prints a line with the message shown
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("You are already logged in")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    flash("Logout successful", "Information")
    session.pop("user", None) #removes data once logged out so nobody else can see
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        #return f"<h1>{user}</h1>" #prints the user's name on the screen
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email has been saved successfully")
        else:
            if "email" in session:
                email = session["email"]
                
        return render_template("flaskindex.html", user=user, email=email)
    else:
        flash("You are not logged in yet, you should login in for full access to all features")
        return redirect(url_for("login"))

@app.route('/play')
def playsong():
    song.funkymusic("Kanskaart - Congratulations (100K Special).mp3")

if __name__ == "__main__":
    db.create_all() #creates the database in case it doesn't already exist
    app.run(debug=True)
