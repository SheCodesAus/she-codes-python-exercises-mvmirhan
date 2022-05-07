# Ask the user to enter a string. Output the string one character at a time, as well as it’s position in the string.

string_value=input("Please enter a string: ")

#This was just added to step through the process
print(len(string_value)) #returns the number of character in the variable
print(range(len(string_value))) #returns the range based from the number of characters in the variable

for pos in range(len(string_value)):
    print(pos, string_value[pos])

