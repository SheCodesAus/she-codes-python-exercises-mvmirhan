# Write a program that asks the user to enter their email address and checks whether it is valid or not. For
# the purpose of this exercise, you can make the assumption that a valid email address contains a “@” symbol
# and a “.” symbol.

email_add=input("Enter your email address: ")

if "@" and "." in email_add:
    print("Valid")
else: print ("Invalid")







