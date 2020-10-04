from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)
import pyserver as song

@app.route("/<name>")
def homepage(name):
    return render_template("flaskindex.html", content=name)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"] #gets the data from the 'nm' key in a dictionary
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    print(usr)
    return f"<p>{usr}</p>"

@app.route('/play')
def playsong():
    song.funkymusic("Kanskaart - Congratulations (100K Special).mp3")

if __name__ == "__main__":
    app.run(debug=True)
