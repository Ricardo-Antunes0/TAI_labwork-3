import os

def main():
    os.chdir('../bin/')
    musics_dir = '../musics/'
    signatures_dir = '../signatures/musics/'
    for file in os.listdir(musics_dir):
        if file.endswith('.wav'):
            output_filename = signatures_dir + file[:-4] + '.bin'
            command = 'GetMaxFreqs.exe -w "' + output_filename + '" "' + musics_dir + file + '"'
            os.system(command)

if __name__ == '__main__':
    main()