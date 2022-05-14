# Using the same colour csv files,
# write a program that outputs the number of times each of the following
# colours appear in the English Name:
# ● red
# ● green
# ● blue
# ● yellow

list_words = ["red","green","blue","yellow"]
red_total = 0
green_total = 0
blue_total = 0
yellow_total = 0

import csv

#q4.1
# with open("csv_files/colours_20.csv", encoding="utf-8") as colours_20_obj:
#     reader = csv.reader(colours_20_obj)
#q4.2
with open("csv_files/colours_213.csv", encoding="utf-8") as colours_213_obj:
    reader = csv.reader(colours_213_obj)

    for line in reader:
        if list_words[0] in line[4].lower():
            red_total += 1
        if list_words[1] in line[4].lower():    
            green_total += 1
        if list_words[2] in line[4].lower():      
            blue_total += 1
        if list_words[3] in line[4].lower():     
            yellow_total += 1

print(f"Red: {red_total}")
print(f"Green: {green_total}")
print(f"Blue: {blue_total}")
print(f"Yellow: {yellow_total}")

# print(line[4]) #Use index; this is how you can print each column
# is_header=False #To initiliase the first value

#Method 1: this is to skip a row(removed the header in this example); 
# next(reader) 

#Method 2
        # if is_header==True:
        #     print(line)
        # is_header = True #This is to define the next value for is_header which is inside the loop      
#         for item in line[4]:
#             # print(item)



