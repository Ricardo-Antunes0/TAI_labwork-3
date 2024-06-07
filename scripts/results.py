import os
import matplotlib.pyplot as plt

def main():
    # generate results for all samples
    for compressor in ["gzip", "bzip2", "lzma"]:
        for sample in os.listdir("../samples"):
            if sample.endswith(".wav"):
                os.system(f"python labwork3.py -c {compressor} -o ../results/{compressor}.csv ../samples/{sample}")

if __name__ == "__main__":
    main()