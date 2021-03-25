import csv


class Pokedex:
    def readFile(self):
        print("hello")





file_to_open = "pokemon.csv"
with open(file_to_open,'r', encoding ="utf8") as this_csv_file:
    this_csv_reader = csv.reader(this_csv_file, delimiter=".")
    header = next(this_csv_reader)
    print(header)