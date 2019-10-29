import sqlite3

DB_FILE="accounts.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()
#c = sqlite3.connect('accounts.db', check_same_thread=False).cursor()
c.execute('''CREATE TABLE IF NOT EXISTS USERNAMES(
            [userID] INTEGER PRIMARY KEY, [username] text NOT NULL, [password] text);''')
           # Creates table if usernames do not exist
c.execute('''CREATE TABLE IF NOT EXISTS STORIES
             ([storyID] INTEGER PRIMARY KEY, [title] text NOT NULL);''')
           # Creates table if stories do not exist
c.execute('''CREATE TABLE IF NOT EXISTS STORYEDITS
             ([storyID] INTEGER, [userID] INTEGER, [text] text NOT NULL);''')
           # Creates table if storyedits do not exist
c.execute('''INSERT INTO STORIES VALUES(0, "title");''') # Story values stored in table
c.execute('''INSERT INTO USERNAMES VALUES(0, "username", "password");''') # Username values stored in a table
c.execute('''INSERT INTO STORYEDITS VALUES(0, 0, "text");''') #Storyedit values stored in a table


db.commit() #save changes
db.close()
