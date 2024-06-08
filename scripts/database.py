import sqlite3
import os

conn = sqlite3.connect('../labwork3.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Music (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        signature TEXT NOT NULL
    )
''')

for file in os.listdir('../signatures/'):
    if file.endswith('.bin'):
        # remove the .bin extension and the number in the beginning of the file name
        name = file[:-4].split('-', 1)[1]
        signature = open('../signatures/' + file, 'rb').read()
        cursor.execute('''
            INSERT INTO Music (name, signature)
            VALUES (?, ?)
        ''', (name, signature))

conn.commit()
conn.close()