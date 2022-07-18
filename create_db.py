import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()


# Create table emails

cur.execute('''
CREATE TABLE emails
(UserName varchar(255), Email varchar(128) UNIQUE)
''')

# Create table phones

cur.execute('''
CREATE TABLE phones
(UserName varchar(255), Phone varchar(128) UNIQUE)
''')

conn.commit()
conn.close()

