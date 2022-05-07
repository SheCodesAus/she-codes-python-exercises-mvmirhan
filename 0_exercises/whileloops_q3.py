
# Q3: Select a number. Ask the user to enter a number, output whether their number is less than or greater than
# the selected number. Repeat this process until the user guesses the correct number.

#Let i be any number used as a number for user to guess
i = 25         
num=int(input("Guess a number: "))

#Use while loop to repeat code until a user guess the right number
while num!=i:
    if num<i:
        print("Too low")
        # num=int(input("Guess a number: "))   #added to break the while loop and to ask the user to guess the number again
    elif num>i:
        print("Too high")
    num=int(input("Guess a number: "))        #Tab out from if statement to break the loop
else: num=i       #Best practice to add the else 
print("Correct")

