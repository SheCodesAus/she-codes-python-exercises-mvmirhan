# Ask the user for a number.
# Use a for loop to print the times tables for that number

num=int(input("enter a number: "))
for count in range(1,num+1):   #stop should match number I entered num + 1
    print(num, "x", count, "=", num * count)
    # print(f"{num} * {count} = {num * count}") #Asli's way



