import sqlite3
import gzip
import bz2
import lzma
import argparse
import sys
import os

def write_results_csv(output_filename, file, music_id, predicted_id, distance, compressor):
    if not os.path.exists(output_filename):
        with open(output_filename, "w") as f:
            f.write("filename,music_id,predicted_id,distance,compressor\n")
    
    with open(output_filename, "a") as f:
        f.write(f"{file},{music_id},{predicted_id},{distance},{compressor}\n")

def ncd(x,y, compressor):
    if compressor == "gzip":
        compress = gzip.compress
    elif compressor == "bzip2":
        compress = bz2.compress
    elif compressor == "lzma":
        compress = lzma.compress
    
    xy = x + y

    Cx = compress(x)
    Cx_bits = len(Cx) * 8

    Cy = compress(y)
    Cy_bits = len(Cy) * 8

    Cxy = compress(xy)
    Cxy_bits = len(Cxy) * 8

    cdn = (Cxy_bits - min(Cx_bits, Cy_bits)) / max(Cx_bits, Cy_bits)
    return cdn

def main(music_file, compressor, output_filename):
    print(f"Analyzing {music_file}")
    print(f"Using {compressor} compressor")

    os.chdir('../bin/')
    os.system(f"GetMaxFreqs.exe -w temp.bin {music_file}")

    file_signature = open("temp.bin", "rb").read()

    musics = {}
    # for music in database extract the name and the signature
    conn = sqlite3.connect('../labwork3.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, signature FROM Music")
    for row in cursor:
        db_signature = row[2]
        distance = ncd(file_signature, db_signature, compressor)
        musics[row[0]] = {"name": row[1], "distance": distance}
    
    min_distance = min(musics.values(), key=lambda x: x["distance"])
    min_id = min(musics, key=lambda x: musics[x]["distance"])
    print(f"Music: {min_distance['name']}\nDistance: {min_distance['distance']}")

    filename = music_file.split("/")[-1] if "/" in music_file else music_file.split("\\")[-1]
    cursor.execute("SELECT music_id FROM Sample WHERE name = ?", (filename,))
    music_id = cursor.fetchone()[0]
    if music_id:
        if music_id == min_id:
            print("Correct answer!")
        else:
            cursor.execute("SELECT name FROM Music WHERE id = ?", (music_id,))
            correct_music = cursor.fetchone()[0]
            print("Incorrect answer! The correct music is", correct_music)

    if output_filename:
        write_results_csv(output_filename, filename, music_id, min_id, min_distance["distance"], compressor)

    os.remove("temp.bin")
    
parser = argparse.ArgumentParser()
parser.add_argument('music_file', help='The path to the music file')
parser.add_argument('-c', '--compressor', choices=['gzip', 'bzip2', 'lzma'], help='The type of compressor to use (gzip, bzip2, lzma)')
parser.add_argument('-o', '--output', help='The output filename')
args = parser.parse_args()

if __name__ == "__main__":
    if not os.path.exists(args.music_file):
        print("File not found!")
        sys.exit(1)
    
    compressor = args.compressor if args.compressor else 'gzip'
    output_filename = args.output

    main(args.music_file, compressor, output_filename)