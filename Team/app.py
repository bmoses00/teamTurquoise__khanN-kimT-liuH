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
c = db.cursor()
#c = sqlite3.connect('accounts.db', check_same_thread=False).cursor()
c.execute('''CREATE TABLE IF NOT EXISTS USERNAMES(
            [id] INTEGER PRIMARY KEY, [username] text NOT NULL, [password] text);''')
c.execute('''CREATE TABLE IF NOT EXISTS STORIES
             ([id] INTEGER PRIMARY KEY, [title] text NOT NULL, [TEXT] text, [Date] text);''')
#c.execute('''
#     INSERT INTO STORIES VALUES(1, "The Green Pancake", "blah blah blah", "2019-09-10");
# ''')
#c.execute('''
#     INSERT INTO USERNAMES VALUES(1, "username", "password");
# ''')
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
            reason = "Invalid credentials"
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
                reason = "Invalid credentials"
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
            if (dbFunctions.addUser(username,password)):
                dbFunctions.addUser(username,password)
                return redirect(url_for("success"))
        if (password != password2):
            reason = "Passwords don't match"
            flash(reason)

        else:
            reason = "Username taken, try again"
            flash(reason)

    return render_template('signup.html')


@app.route("/createStory")
def createStory():
    global reason
    if ("title" in request.args) & ("text" in request.args) & ("date" in request.args):
        title = request.args["title"]
        text = request.args["text"]
        date = request.args["date"]
        if (dbFunctions.addStory(title, text, date)):
            dbFunctions.addStory(title, text, date)
            return redirect(url_for("success"))
        else:
            reason = "ERROR, Enter a different title"
            flash(reason)

    return render_template('createStory.html')


@app.route("/addToStory")
def addToStory():
    global reason
    if ("id" in request.args) & ("text" in request.args):
        id = request.args["id"]
        text = request.args["text"]
        if (dbFunctions.editStory(id, text)):
            dbFunctions.editStory(id, text)
            return redirect(url_for("success"))
        else:
            reason = "ERROR"
            flash(reason)
    return render_template('addToStory.html')

@app.route("/loggedIn")
def success():
    return render_template(
        "loggedIn.html",
        storylist = dbFunctions.getStory()
        )


db.commit() #save changes
db.close()

# page for creating a new story

if __name__ == "__main__":
    app.debug = True
    app.run()
