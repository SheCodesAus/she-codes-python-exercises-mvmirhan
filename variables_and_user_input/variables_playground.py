from turtle import clear


weather = "rainy"  #weather is a variable, rainy is the data
name = "Marivic"

# print ("rainy")
# print (weather)

# Data Types
# String is a text data. Requires a ""
# Integer: Numerical data, whole numbers
# Float: Numerical data (with decimals)

height = 155
weight = 55.8
# print(type(name))
# print(type(height))
# print(type(weight))

day = "Saturday"
print(type(day))
message = f"Today is {day}!"
# print(message)

message2 = "Today is " + day
# print(message2)
# print(message)

message3 = "Today is {day}" #without the function, the curly brackets treats the day as a string
# print(message3)

#Integers
#Run distance in m
run1_dist = 1400
run2_dist = 1800

#Addition
total_dist = run1_dist + run2_dist
# print(total_dist)

#Floats
#Run distance in km
run3_dist = 1.7
run4_dist = 6.35
total_dist = run3_dist + run4_dist
# print(total_dist)

#Division and Multiplication
print(run1_dist/1000)
print(run1_dist*1000)

#Division always produced float
#Other operations depends on the data type
#As long as there is one float, float will be the output

#Different scenarios
name = "Marivic"
# print (name + run2_dist)
# print (name * run2_dist)
# print (name * run3_dist)

#Typecast to change the data type
# print (name + str(run3_dist))
# print (name * int(run3_dist))
print (name * int(run4_dist))


