from os.path import exists
from csv import DictReader

# file = open("files.txt", "r", encoding="utf-8")
# data = file.read()
# file.close()
# print(data)

# context manager
if exists("files.txt"):
    with open("files.txt", "r", encoding="utf-8") as file:
        data = file.read()
    print(data)
else:
    print("File doesnt exist!")

with open("my-first-csv.csv", "r", encoding="utf-8") as f:
    csv_reader = DictReader(f)
    data = [row for row in csv_reader]

print(data)