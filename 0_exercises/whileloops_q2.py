# Ask the user to enter a string. Output the string one character at a time, as well as it’s position in the string.

from calendar import c
from lib2to3.pgen2.token import AT
from re import A, T


string_value=input("Please enter a string: ")

for pos in range(len(string_value)):
    print(pos)

for char in string_value:
    print(char)

#Current output
# 0
# 1
# 2
# 3
# a
# a
# t
# s
#I'M STUCK HERE. 
