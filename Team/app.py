from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
import os

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("login.html")

@app.route("/signup")
def success():
    return render_template(
        "signup.html"
        )

# page for creating a new story

if __name__ == "__main__":
    app.debug = True
    app.run()
