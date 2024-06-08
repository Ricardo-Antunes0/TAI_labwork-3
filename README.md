# TAI Group #4
## Third project
## Developed by:
- Pompeu Costa, 103294
- Rafael Pinto, 103379
- Ricardo Antunes, 98275

## How to run the labwork3 script

Inside the scripts directory, run the following command:

```bash
python labwork3 labwork3.py [-h] [-c {gzip,bzip2,lzma}] [-o OUTPUT] music_file

```

Note: the script will only work in Windows, as it uses the `GetMaxFreqs.exe` executable. To run the script in Linux, it is necessary to change the `GetMaxFreqs.exe` to `GetMaxFreqs` in the script.

## Parameters

### Positional arguments
- `music_file`: The path to the music file to be analyzed.

### Optional arguments
- `-h, --help`: Show the help message and exit.
- `-c {gzip,bzip2,lzma}, --compressor {gzip,bzip2,lzma}`: The type of compressor to be used. Default is `gzip`.
- `-o OUTPUT, --output OUTPUT`: The path to the output file. If not specified, there will be no output file.