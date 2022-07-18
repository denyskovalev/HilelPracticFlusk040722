import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()


# Create table

cur.execute('''
CREATE TABLE emails
(UserName varchar(255), Email varchar(128) UNIQUE)
''')

conn.commit()
conn.close()

