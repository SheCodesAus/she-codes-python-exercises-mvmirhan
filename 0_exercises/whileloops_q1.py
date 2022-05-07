# Continuously ask the user to enter a number until they provide a blank input. 
# Output the sum of all the numbers.

number = input("Enter a number: ") #to initialize user to enter first number
sum=0
while number != "":                
    sum = sum + int(number)
    number = input("Enter a number: ") #to ask user for another number
print (sum)

#The code wont work if the variable inside the while loop is typecast as an integer

# number = int(input("Enter a number: ")) #to initialize user to enter first number
# sum=0
# while number != "":                
#     sum = sum + int(number)
#     number = (input("Enter a number: ")) #to ask user for another number
# print (sum)