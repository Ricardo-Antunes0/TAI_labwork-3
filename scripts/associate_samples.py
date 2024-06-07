import sqlite3

conn = sqlite3.connect('../labwork3.db')

cursor = conn.cursor()

cursor.execute('''
    DROP TABLE IF EXISTS Sample
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sample (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        music_id INTEGER NOT NULL,
        FOREIGN KEY (music_id) REFERENCES Music(id)
    )
''')

cursor.execute('''
    INSERT INTO Sample (name, music_id)
    VALUES
    ('sample01.wav', 1),
    ('sample02.wav', 12),
    ('sample03.wav', 23),
    ('sample04.wav', 34),
    ('sample05.wav', 45),
    ('sample06.wav', 47),
    ('sample07.wav', 48),
    ('sample08.wav', 49),
    ('sample09.wav', 50),
    ('sample10.wav', 2),
    ('sample11.wav', 3),
    ('sample12.wav', 4),
    ('sample13.wav', 5),
    ('sample14.wav', 6),
    ('sample15.wav', 7),
    ('sample16.wav', 8),
    ('sample17.wav', 9),
    ('sample18.wav', 10),
    ('sample19.wav', 11),
    ('sample20.wav', 13),
    ('sample21.wav', 14),
    ('sample22.wav', 15),
    ('sample23.wav', 16),
    ('sample24.wav', 17),
    ('sample25.wav', 18),
    ('sample26.wav', 19),
    ('sample27.wav', 20),
    ('sample28.wav', 21),
    ('sample29.wav', 22),
    ('sample30.wav', 24),
    ('sample31.wav', 25),
    ('sample32.wav', 26),
    ('sample33.wav', 27),
    ('sample34.wav', 28),
    ('sample35.wav', 29),
    ('sample36.wav', 30),
    ('sample37.wav', 31),
    ('sample38.wav', 32),
    ('sample39.wav', 33),
    ('sample40.wav', 35),
    ('sample41.wav', 36),
    ('sample42.wav', 37),
    ('sample43.wav', 38),
    ('sample44.wav', 39),
    ('sample45.wav', 40),
    ('sample46.wav', 41),
    ('sample47.wav', 42),
    ('sample48.wav', 43),
    ('sample49.wav', 44),
    ('sample50.wav', 46)
''')

conn.commit()
conn.close()
               