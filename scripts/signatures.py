import os

def main():
    entire_musics()
    #samples()

def entire_musics():
    os.chdir('../bin/')
    musics_dir = '../musics/'
    signatures_dir = '../signatures/musics/'
    for file in os.listdir(musics_dir):
        if file.endswith('.wav'):
            output_filename = signatures_dir + file[:-4] + '.bin'
            command = 'GetMaxFreqs.exe -w "' + output_filename + '" "' + musics_dir + file + '"'
            os.system(command)

def samples():
    os.chdir('../bin/')
    samples_dir = '../samples/'
    signatures_dir = '../signatures/samples/'
    for file in os.listdir(samples_dir):
        if file.endswith('.wav'):
            os.system('GetMaxFreqs.exe -w ' + signatures_dir + file[:-4] + '.bin ' + samples_dir + file)

if __name__ == '__main__':
    main()