import sqlite3

DB_FILE="accounts.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()
#c = sqlite3.connect('accounts.db', check_same_thread=False).cursor()
c.execute('''CREATE TABLE IF NOT EXISTS USERNAMES(
            [id] INTEGER PRIMARY KEY, [username] text NOT NULL, [password] text);''')
c.execute('''CREATE TABLE IF NOT EXISTS STORIES
             ([id] INTEGER PRIMARY KEY, [title] text NOT NULL, [TEXT] text, [Date] text);''')
c.execute('''INSERT INTO STORIES VALUES(1, "The Green Pancake", "blah blah blah", "2019-09-10");''')
c.execute('''
     INSERT INTO USERNAMES VALUES(1, "username", "password");
 ''')


db.commit() #save changes
db.close()
