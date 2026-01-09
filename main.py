import csv

def csvParser():
    with open("WavelengthCopy/Spectrums/default.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            print(row[0],"Middle", row[1])


def main():
    print("The category is:")
    csvParser()

if __name__ == "__main__":
    main()


