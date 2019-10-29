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

def addStory(title, userID, text):
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
        command = "INSERT INTO STORIES VALUES({}, \"{}\");".format(q[len(q)-1][0]+1,title)
        c.execute(command)
        command = "INSERT INTO STORYEDITS VALUES({}, \"{}\",\"{}\");".format(q[len(q)-1][0]+1,userID,text)
        c.execute(command)
        db.commit() #save changes
        db.close()  #close database
        return True
    else:
        db.commit() #save changes
        db.close()  #close database
        return False
#def canADD(storyID, userID)
def addToStory(storyID, userID, text):
    DB_FILE="accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT storyID, storyID FROM STORIES WHERE storyID = \"{}\";".format(storyID)
    c.execute(command)
    new = c.fetchall()
    if len(new) == 1:
        command = "SELECT storyID FROM STORYEDITS;"
        c.execute(command)
        q = c.fetchall()
        command = "INSERT INTO STORYEDITS VALUES(\"{}\",\"{}\",\"{}\");".format(storyID,userID,text)
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

def almagate(): #the list it returns should be in order
    DB_FILE="accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM STORYEDITS;"
    c.execute(command)
    new = c.fetchall()
    command = "SELECT storyID FROM STORIES;"
    c.execute(command)
    storyIDs = c.fetchall()
    l = []
    oldtext = ""
    for storyID in storyIDs:
        print (storyID)
        for row in new:
            print (row)
            if storyID[0] == row[0]:
                oldtext += row[2]
        l.append(oldtext)
        oldtext = ""
    db.commit() #save changes
    db.close()  #close database
    return l

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
