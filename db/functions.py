import sqlite3
import random
import string

def randomcode():
    letters = string.ascii_lowercase
    code = ''.join(random.choice(letters) for i in range(5))

    conn = sqlite3.connect('db/database.db')
    cursor = conn.execute(f"SELECT code FROM notes WHERE code = '{code}'")
    
    return code if cursor.fetchone() is None else randomcode()

def create_note(code, note):
    conn = sqlite3.connect('db/database.db')
    conn.execute(f"INSERT INTO notes (code, note) VALUES ('{code}', '{note}')")
    conn.commit()
    conn.close()
    return True

def read_note_by_code(code):
    conn = sqlite3.connect('db/database.db')
    cursor = conn.execute(f"SELECT note FROM notes WHERE code = '{code}'")
    note = cursor.fetchone()
    conn.close()
    return note[0] if note else None

def update_note_by_code(code, note):
    conn = sqlite3.connect('db/database.db')
    conn.execute(f"UPDATE notes SET note = '{note}' WHERE code = '{code}'")
    conn.commit()
    conn.close()
    return True