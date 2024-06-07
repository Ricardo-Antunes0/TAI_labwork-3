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
    ('sample01', 1),
    ('sample02', 12),
    ('sample03', 23),
    ('sample04', 34),
    ('sample05', 45),
    ('sample06', 47),
    ('sample07', 48),
    ('sample08', 49),
    ('sample09', 50),
    ('sample10', 2),
    ('sample11', 3),
    ('sample12', 4),
    ('sample13', 5),
    ('sample14', 6),
    ('sample15', 7),
    ('sample16', 8),
    ('sample17', 9),
    ('sample18', 10),
    ('sample19', 11),
    ('sample20', 13),
    ('sample21', 14),
    ('sample22', 15),
    ('sample23', 16),
    ('sample24', 17),
    ('sample25', 18),
    ('sample26', 19),
    ('sample27', 20),
    ('sample28', 21),
    ('sample29', 22),
    ('sample30', 24),
    ('sample31', 25),
    ('sample32', 26),
    ('sample33', 27),
    ('sample34', 28),
    ('sample35', 29),
    ('sample36', 30),
    ('sample37', 31),
    ('sample38', 32),
    ('sample39', 33),
    ('sample40', 35),
    ('sample41', 36),
    ('sample42', 37),
    ('sample43', 38),
    ('sample44', 39),
    ('sample45', 40),
    ('sample46', 41),
    ('sample47', 42),
    ('sample48', 43),
    ('sample49', 44),
    ('sample50', 46)
''')

conn.commit()
conn.close()
               