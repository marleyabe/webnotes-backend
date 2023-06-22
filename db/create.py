import sqlite3

conn = sqlite3.connect('db/database.db')

conn.execute("""CREATE TABLE notes (
            code TEXT UNIQUE,
            note TEXT)""")

print ("Table created successfully")
conn.close()