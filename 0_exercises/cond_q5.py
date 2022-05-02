# Write a program that asks the user to enter their username and password, 
# and outputs a success message if they are correct, or a failure message if they are incorrect.


username = "fleur"
password = "password123"

username=(input("Enter your username: "))
password=(input("Enter your password: "))

if (username=="fleur") and (password=="password123"):
    print ("Correct!")
else: print ("Incorrect")