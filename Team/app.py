from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
from utl import dbFunctions
import sqlite3
import os


DB_FILE="accounts.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
#c = db.cursor()
#c = sqlite3.connect('accounts.db', check_same_thread=False).cursor()

app = Flask(__name__)
app.secret_key = os.urandom(32)
reason = ""

@app.route("/")
def root():
    #global is a keyword that allows an user to modify a variable outside the current scope
    global reason
    print(url_for("success"))
    #Check to see if user entered usernamee and password
    if ("username" in request.args) & ("password" in request.args):
        username = request.args["username"]
        password = request.args["password"]
        #If password and usernamee are correct
        if (dbFunctions.accountExists(username,password) > -1):
            return redirect(url_for("success"))
        #If credentials incorrect
        else:
            reason = "invalid"
            flash(reason)
            return redirect(url_for("try_again"))
    return render_template(
    'login.html'
        )


#If password or usernamee is incorrect
@app.route("/error")
def try_again():
    global reason
    if ("username" in request.args) & ("password" in request.args):
            username = request.args["username"]
            password = request.args["password"]
            #If password and usernamee are correct
            if (dbFunctions.accountExists(username,password) > -1):
                return redirect(url_for("success"))
            #If credentials incorrect
            else:
                reason = "invalid"
                flash(reason)
                return redirect(url_for("try_again"))
    return render_template(
        'error.html',reasonforError=reason
    )

@app.route("/signup")
def signup():
    global reason
    if ("username" in request.args) & ("password" in request.args) & ("password2" in request.args):
        password = request.args["password"]
        password2 = request.args["password2"]
        username = request.args["username"]
        if (password == password2):
            dbFunctions.addUser(username,password)
            return redirect(url_for("success"))
    return render_template('signup.html')

@app.route("/loggedIn")
def success():
    return render_template(
        "loggedIn.html"
        )


db.commit() #save changes
db.close()

# page for creating a new story

if __name__ == "__main__":
    app.debug = True
    app.run()
