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

for file in os.listdir('../signatures/musics/'):
    if file.endswith('.bin'):
        # remove the .bin extension and the number in the beginning of the file name
        name = file[:-4].split('-', 1)[1]
        signature = open('../signatures/musics/' + file, 'rb').read()
        cursor.execute('''
            INSERT INTO Music (name, signature)
            VALUES (?, ?)
        ''', (name, signature))

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sample (
        id INTEGER PRIMARY KEY,
        file TEXT NOT NULL,
        name TEXT NOT NULL,
        seconds INTEGER NOT NULL,
        signature TEXT NOT NULL
    )
''')

for file in os.listdir('../signatures/samples/'):
    if file.endswith('.bin'):
        filename = file[:-4] + '.wav'
        # search for name in md file and extract the name and the seconds
        music_name = ""
        seconds = 0
        with open('../samples/samples.md', 'r') as f:
            for line in f:
                if filename in line:
                    music_name = line.split('|')[2].strip()
                    seconds = int(line.split('|')[3].strip()[:-1])
                    break
        signature = open('../signatures/samples/' + file, 'rb').read()
        cursor.execute('''
            INSERT INTO Sample (file, name, seconds, signature)
            VALUES (?, ?, ?, ?)
        ''', (filename, music_name, seconds, signature))

conn.commit()
conn.close()