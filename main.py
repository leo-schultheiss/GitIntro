import csv

def main():
    print("Hello World!")

    csv_path = "data.csv"
    with open(csv_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)

if __name__ == "__main__":
    main()
