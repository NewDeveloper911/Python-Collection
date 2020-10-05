from flask import Flask

secmessage = "omae wo mo shinderu"
app = Flask(__name__)

@app.route("/")
def get_secret_message():
	return secmessage
