from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
import pyserver as song

@app.route("/<name>")
def homepage(name):
    return render_template("flaskindex.html", content=name)
'''    
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"
    
@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))
'''

@app.route('/play')
def playsong():
    song.funkymusic("Kanskaart - Congratulations (100K Special).mp3")

if __name__ == "__main__":
    app.run(debug=True)
