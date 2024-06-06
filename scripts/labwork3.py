import sqlite3
import gzip
import sys
import os

def cdn(x,y):
    xy = x + y

    Cx = gzip.compress(x)
    Cx_bits = len(Cx) * 8

    Cy = gzip.compress(y)
    Cy_bits = len(Cy) * 8

    Cxy = gzip.compress(xy)
    Cxy_bits = len(Cxy) * 8

    cdn = (Cxy_bits - min(Cx_bits, Cy_bits)) / max(Cx_bits, Cy_bits)
    return cdn

def main(music_file):
    os.chdir('../bin/')
    os.system(f"GetMaxFreqs.exe -w temp.bin {music_file}")

    file_signature = open("temp.bin", "rb").read()

    musics = {}
    # for music in database extract the name and the signature
    conn = sqlite3.connect('../labwork3.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, signature FROM Music")
    for row in cursor:
        db_signature = row[1]
        distance = cdn(file_signature, db_signature)
        musics[row[0]] = distance
    conn.close()
    
    for music, distance in musics.items():
        print(f"{music}: {distance}")

    min_distance = min(musics.values())
    print(f"The most similar music is {min(musics, key=musics.get)} with distance {min_distance}")

    os.remove("temp.bin")
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python3 labwork3.py <music_file>")    