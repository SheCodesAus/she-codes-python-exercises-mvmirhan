print("Ask the user for a number and use this to generate a pyramid of that height.")

pyramid_height = int(input("Enter a number: "))

for i in range(pyramid_height):
    for j in range (i+1):
        print("* ",end="")
    print("\n")    #This means a new line or end line