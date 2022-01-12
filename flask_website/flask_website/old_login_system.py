#This is my old login system, which all can use if the new login system doesn't work on your device

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
            app.logger.info("You should be logged in as an existing user")
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit() #commits change to databse. like git
            app.logger.info("Welcome to the party, mi amigo")
            
        flash("Login successful!") #prints a line with the message shown
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("You are already logged in")
            app.logger.info("Oi, hombre. You are already logged in")
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
            app.logger.info("Email has been saved successfully")
        else:
            if "email" in session:
                email = session["email"]
                app.logger.info("Email has been set firmly")
            else:
                app.logger.info("I'm currently lacking your email and resignation letter, you dunce")
                
        return render_template("flaskindex.html", user=user, email=email)
    else:
        app.logger.info("tried to skip the queue, huh? You are a fool, mi compadre.")
        flash("You are not logged in yet, you should login in for full access to all features")
        return redirect(url_for("login"))
