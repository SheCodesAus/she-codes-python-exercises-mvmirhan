import csv

# with open("csv_files/2016_pilbara.csv") as csv_file:  #add the folder name (csv_files)
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line)

population = []

with open("csv_files/2016_pilbara.csv", encoding="utf-8") as csv_file_a:
    reader = csv.reader(csv_file_a) 
    # print(reader)
    #reader this is a variable (object); referring to a library (csv.reader function) to take in the file
    for line in reader: #line is any name i assigned to store the result
        #required to iterate over each row; for each row create an empty list; separates elements based on the delimiter
        #print(line)
        population.append(line)

# print(population)
# print()

# for age_group in population:
#     print(f"{age_group[0]} {age_group[1]}")

# # writing to csv file
# with open("csv_files/population.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")
#     for age_group in population:
        # csv_writer.writerow([age_group[1], age_group[0]])




