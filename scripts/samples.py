import os
import subprocess
import random
import sqlite3

musics_dir = '../musics/'
conn = sqlite3.connect('../labwork3.db')

sample = 51
for file in os.listdir(musics_dir):
    start = 0
    end = random.randint(10, 20)
    if "jingle.tm" in file or "ft." in file:
        music_name = file.split('.')[0] + '.' + file.split('.')[1].split('.')[0]
        music_name = music_name.split('-')[1] + '-' + music_name.split('-')[2]
    elif "Master of Puppets" in file:
        music_name = "Master of Puppets"
    elif "Heart-Shaped Box" in file:
        music_name = "Nirvana - Heart-Shaped Box"
    elif "Guns N Roses - Knockin On Heavens Door" in file:
        music_name = "Guns N Roses Knockin On Heavens Door"
    elif "Queen Bohemian Rhapsody" in file:
        music_name = "Queen Bohemian Rhapsody"
    elif "Rosinha - Eu Descasco-lhe A Banana" in file:
        music_name = "Rosinha - Eu Descasco-lhe A Banana"
    elif "Mozart - Requiem - Sanctus - Herreweghe" in file:
        music_name = "Mozart - Requiem - Sanctus - Herreweghe"
    elif "Beethoven 5th Symphony in C Minor Op.67- Herbert Von Karajan" in file:
        music_name = "Beethoven 5th Symphony in C Minor Op.67- Herbert Von Karajan"
    else:
        music_name = file.split('.')[0].split('-')[1] + '-' + file.split('.')[0].split('-')[2]
    cursor = conn.cursor()
    cursor.execute(f"SELECT id FROM Music WHERE name = '{music_name}'")
    music_id = cursor.fetchone()[0]
    print(f"Music: {music_name}\tID: {music_id}")

    audio_length = int(float(subprocess.check_output(f'sox --i -D "{musics_dir}{file}"', shell=True).decode('utf-8').strip()))

    while end < audio_length:
        sample_filename = f"sample{sample}.wav"
        # trim audio files into 10-20 seconds random samples using sox
        os.system(f'sox "{musics_dir}{file}" ../samples/sample{sample}.wav trim {start} {end - start}')
        seconds = end - start
        start = end + random.randint(5, 10) # 5-10 seconds between samples
        end = start + random.randint(10, 20)
        conn.execute("INSERT INTO Sample (name, music_id) VALUES (?, ?)", (sample_filename, music_id))
        conn.commit()
        with open('../samples/samples.md', 'a') as f:
            f.write(f"| {sample_filename} | {music_name} | {seconds} |\n")
        sample += 1
    
conn.close()
