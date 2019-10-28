import sqlite3
import csv

def accountExists(username, password):
    DB_FILE= "accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT userID, username FROM USERNAMES WHERE username = \"{}\" AND password = \"{}\";".format(username, password)
    c.execute(command)
    q = c.fetchall()
    db.commit() #save changes
    db.close()  #close database
    if len(q) == 0:
        return -1 #return -1 if it doesn't exist
    else:
        return q[0][0] #return ID of user if exists


def userExists(username):
    DB_FILE="accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT userID, username FROM USERNAMES WHERE username = \"{}\";".format(username)
    c.execute(command)
    q = c.fetchall()
    db.commit() #save changes
    db.close()  #close database
    if len(q) == 0:
        return -1 #return -1 if it doesn't exist
    else:
        return q[0][0] #return ID of user if exists

def addUser(username, password):
    DB_FILE="accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT userID, username FROM USERNAMES WHERE username = \"{}\";".format(username)
    c.execute(command)
    new = c.fetchall()
    if len(new) == 0:
        command = "SELECT userID FROM USERNAMES;"
        c.execute(command)
        q = c.fetchall()
        command = "INSERT INTO USERNAMES VALUES({}, \"{}\", \"{}\");".format(q[len(q)-1][0]+1,username,password)
        c.execute(command)
        db.commit() #save changes
        db.close()  #close database
        return True
    else:
        db.commit() #save changes
        db.close()  #close database
        return False

def addStory(title, text, date):
    DB_FILE="accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT storyID, title FROM STORIES WHERE title = \"{}\";".format(title)
    c.execute(command)
    new = c.fetchall()
    if len(new) == 0:
        command = "SELECT storyID FROM STORIES;"
        c.execute(command)
        q = c.fetchall()
        command = "INSERT INTO STORIES VALUES({}, \"{}\", \"{}\", \"{}\");".format(q[len(q)-1][0]+1,title,text,date)
        c.execute(command)
        db.commit() #save changes
        db.close()  #close database
        return True
    else:
        db.commit() #save changes
        db.close()  #close database
        return False

def editStory(ID, TEXT):
    DB_FILE="accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT storyID, storyID FROM STORIES WHERE storyID = \"{}\";".format(ID)
    c.execute(command)
    new = c.fetchall()
    if len(new) == 1:
        command = "SELECT storyID FROM STORIES;"
        c.execute(command)
        q = c.fetchall()
        command = "UPDATE STORIES SET text = TEXT WHERE storyID = ID;"

        c.execute(command)
        db.commit() #save changes
        db.close()  #close database
        return True
    else:
        db.commit() #save changes
        db.close()  #close database
        return False


def getStory(title):
    DB_FILE="accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = ""
    if len(title) > 0:
        command = "SELECT * FROM STORIES WHERE title = \"{}\";".format(title)
    else:
        command = "SELECT * FROM STORIES;"
    c.execute(command)
    new = c.fetchall()
    db.commit() #save changes
    db.close()  #close database
    return new

def getStory1():
    DB_FILE="accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM STORIES;"
    c.execute(command)
    new = c.fetchall()
    db.commit() #save changes
    db.close()  #close database
    return new
