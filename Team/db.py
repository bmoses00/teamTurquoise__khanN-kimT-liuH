import sqlite3

DB_FILE="accounts.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()
#c = sqlite3.connect('accounts.db', check_same_thread=False).cursor()
c.execute('''CREATE TABLE IF NOT EXISTS USERNAMES(
            [userID] INTEGER PRIMARY KEY, [username] text NOT NULL, [password] text);''')
c.execute('''CREATE TABLE IF NOT EXISTS STORIES
             ([storyID] INTEGER PRIMARY KEY, [title] text NOT NULL);''')
c.execute('''CREATE TABLE IF NOT EXISTS STORYEDITS
             ([storyID] INTEGER, [userID] INTEGER, [text] text NOT NULL, [Date] text);''')
c.execute('''INSERT INTO STORIES VALUES(0, "The Green Pancake");''')
c.execute('''INSERT INTO USERNAMES VALUES(0, "username", "password");''')
c.execute('''INSERT INTO STORYEDITS VALUES(0, 0, "I am very cool", "2019-10-25");''')


db.commit() #save changes
db.close()
