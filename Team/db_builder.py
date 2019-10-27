import sqlite3   #enable control of an sqlite database
#import csv       #facilitate CSV I/O

#csvFile = ""
DB_FILE="accounts.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
c.execute('''CREATE TABLE IF NOT EXISTS USERNAMES(
            [id] INTEGER PRIMARY KEY, [username] text NOT NULL, [password] text);''')

c.execute('''
    INSERT INTO USERNAMES VALUES(1, "username", "password");
''') #temporary

foo = c.execute('''
    SELECT [username] FROM USERNAMES;
''')
print(foo)

c.execute('''CREATE TABLE IF NOT EXISTS STORIES
             ([id] INTEGER PRIMARY KEY, [title] text NOT NULL, [TEXT] text, [Date] text);''')
c.execute('''
    INSERT INTO STORIES VALUES(1, "The Green Pancake", "blah blah blah", "2019-09-10");
''')


'''
foo = c.execute(q)
print (foo)
'''

db.commit() #save changes
db.close()  #close database
