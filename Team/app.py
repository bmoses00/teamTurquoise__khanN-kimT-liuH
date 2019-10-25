from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
import os

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
        if (password == "1") & (username == "1"):
            return redirect(url_for("signup"))
        #If password and usernamee are correct, say so
        if (password == "1234") & (username == "Peglegs"):
            return redirect(url_for("success"))
        #If password and usernamee are incorrect,
        elif (username != "Peglegs") & (password != "1234"):
            reason = " Your usernamee and password were both incorrect"
            flash(reason)
            return redirect(url_for("try_again"))
        #If usernamee is incorrect, say so
        elif (username != "Peglegs"):
            reason = " Not valid usernamee"
            flash(reason)
            return redirect(url_for("try_again"))
        #If password is incorrect, say so
        else:
            reason = " Your password was incorrect"
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
            #If password and usernamee are correct, say so
            if (password == "1234") & (username == "Peglegs"):
                return redirect(url_for("success"))
            #If password and usernamee are incorrect, say so
            elif (username != "Peglegs") & (password != "1234"):
                reason = " Your username and password were both incorrect"
                return redirect(url_for("try_again"))
            #If usernamee is incorrect, say so
            elif (username != "Peglegs"):
                reason = " Your username was incorrect"
                return redirect(url_for("try_again"))
            #If password is incorrect, say so
            else:
                reason = " Your password was incorrect"
                return redirect(url_for("try_again"))
    return render_template(
        'error.html',reasonforError=reason
    )

@app.route("/signup")
def signup():
    global reason
    if ("password" in request.args) & ("password2" in request.args):
            password = request.args["password"]
            password2 = request.args["password2"]
            if (password == "9"):
                return redirect(url_for("success"))
    return render_template(
        "signup.html"
        )

@app.route("/loggedIn")
def success():
    return render_template(
        "loggedIn.html"
        )




# page for creating a new story

if __name__ == "__main__":
    app.debug = True
    app.run()
