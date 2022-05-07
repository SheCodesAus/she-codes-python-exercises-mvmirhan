import csv
import os

with open("csv_files/dogs.txt") as file:
    file_reader = csv.reader(file,delimiter=" ")
    for row in file_reader:
        print(row)
