import csv
from datetime import datetime

# iso_string = "2021-07-05T07:00:00+08:00"
# date_object = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
# date_format = datetime.strftime(date_object, "%A %d %B %Y")
# print(date_object)
# print(date_format)

# date_string = "12/11/2018"
# date_object = datetime.strptime(date_string, "%d/%m/%Y")
# date_format = datetime.strftime(date_object, "%A %d %B %Y")

# print("date_object =", date_object)
# print("date_format =", date_format)

# def convert_date(iso_string):
#     date_format = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S:%z")
#     return date_format


"""Reads a csv file and stores the data in a list.
    load_data_from_csv("tests/data/example_one.csv")
Args: csv_file: a string representing the file path to a csv file.
Returns: A list of lists, where each sublist is a (non-empty) line in the csv file.

EXPECTED RESULT
========================================
date,min,max
2021-07-02T07:00:00+08:00,49,67
2021-07-03T07:00:00+08:00,57,68
2021-07-04T07:00:00+08:00,56,62
2021-07-05T07:00:00+08:00,55,61
2021-07-06T07:00:00+08:00,53,62
"""
csv_file = [
            ["2021-07-02T07:00:00+08:00", 49, 67],
            ["2021-07-03T07:00:00+08:00", 57, 68],
            ["2021-07-04T07:00:00+08:00", 56, 62],
            ["2021-07-05T07:00:00+08:00", 55, 61],
            ["2021-07-06T07:00:00+08:00", 53, 62] 
      ]







row=0
for item in csv_file:
    append.(csv_file[row])


    
 

# def load_data_from_csv(csv_file): 

#     with open("csv_file", encoding="utf-8") as csv_file_object:
#         reader = csv.reader(csv_file_object)

#     for line in reader:
#         print(line)
    
    # for line in reader:
    #     if list_words[0] in line[4].lower():
    #         red_total += 1
    #     if list_words[1] in line[4].lower():    
    #         green_total += 1
    #     if list_words[2] in line[4].lower():      
    #         blue_total += 1
    #     if list_words[3] in line[4].lower():     
    #         yellow_total += 1

# print(f"Red: {red_total}")
# print(f"Green: {green_total}")
# print(f"Blue: {blue_total}")
# print(f"Yellow: {yellow_total}")







    