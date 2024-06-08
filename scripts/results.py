import os
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score

def main():
    
    # generate results for all samples
    for compressor in ["gzip", "bzip2", "lzma"]:
        for sample in os.listdir("../samples/clean"):
            if sample.endswith(".wav"):
                os.system(f"python labwork3.py -c {compressor} -o ../results/{compressor}.csv ../samples/clean/{sample}")
    
    for compressor in ["gzip", "bzip2", "lzma"]:
        for sample in os.listdir("../samples/noise"):
            if sample.endswith(".wav"):
                os.system(f"python labwork3.py -c {compressor} -o ../results/{compressor}_noise.csv ../samples/noise/{sample}")
    
    print("Clean samples")
    for compressor in ["gzip", "bzip2", "lzma"]:
        predictated = []
        actual = []
        correct = 0 
        total = 0
        with open(f"../results/{compressor}.csv", "r") as f:
            # skip header
            f.readline()
            for line in f.readlines():
                filename, music_id, predicted_id, distance, _ = line.strip().split(",")
                predictated.append(predicted_id)
                actual.append(music_id)
                if music_id == predicted_id:
                    correct += 1
                total += 1
        print(f"Compressor: {compressor}")
        print(f"Accuracy: {correct/total}")
        print(f"Precission: {correct/total}")
        print(f"Recall: {correct/total}")
        print(f"F1 Score: {f1_score(actual, predictated, average='macro')}")
        print(f"Correct: {correct}")
        print(f"Total: {total}")

    print("Noisy samples")
    for compressor in ["gzip", "bzip2", "lzma"]:
        predictated = []
        actual = []
        correct = 0 
        total = 0
        with open(f"../results/{compressor}_noise.csv", "r") as f:
            # skip header
            f.readline()
            for line in f.readlines():
                filename, music_id, predicted_id, distance, _ = line.strip().split(",")
                predictated.append(predicted_id)
                actual.append(music_id)
                if music_id == predicted_id:
                    correct += 1
                total += 1
        print(f"Compressor: {compressor}")
        print(f"Accuracy: {correct/total}")
        print(f"Precission: {correct/total}")
        print(f"Recall: {correct/total}")
        print(f"F1 Score: {f1_score(actual, predictated, average='macro')}")
        print(f"Correct: {correct}")
        print(f"Total: {total}")

if __name__ == "__main__":
    main()