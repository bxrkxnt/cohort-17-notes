from csv import reader, DictReader

if __name__ == "__main__":
    
    f = open("example.csv") # thing that can be read

    # r = reader(f, delimiter=",", quotechar='|') # thing that can read csv-shaped text
    # csv.reader(csvfile, delimiter=' ', quotechar='|')
    r = DictReader(f)

    for l in r:
        print(l)