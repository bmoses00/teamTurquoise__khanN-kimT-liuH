import sqlite3   #enable control of an sqlite database
#import csv       #facilitate CSV I/O

#csvFile = ""
DB_FILE="accounts.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
c.excute('''CREATE TABLE USERNAMES
             ([id] INTEGER, [username] text, [password] text''')

'''
foo = c.execute(q)
print (foo)
'''
db.commit() #save changes
db.close()  #close database
