import sqlite3
import os

conn = sqlite3.connect('../labwork3.db')

for file in os.listdir('../samples/clean'):
    music_id = conn.execute(f"SELECT music_id FROM Sample WHERE name = '{file}'").fetchone()[0]
    output_file = f"whitenoise_{file}"
    # add noise to samples using sox
    os.system(f'sox ../samples/clean/{file} aux.wav synth whitenoise vol 0.1')
    os.system(f'sox -m ../samples/clean/{file} aux.wav ../samples/noise/{output_file}')

    os.remove('aux.wav')

    conn.execute("INSERT INTO Sample (name, music_id) VALUES (?, ?)", (output_file, music_id))
    conn.commit()
    
conn.close()
