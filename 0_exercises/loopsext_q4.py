print("Ask the user for a number and use this to generate a (different) pyramid of that height.")
pyramid_height = int(input("Enter a number: "))
x = 0

for i in range(1,pyramid_height+1):  
    for spacing in range (1,(pyramid_height-i)+1):        
        print(end="  ")  #2 spaces here
    while x!=(2*i-1):
        print("* ",end="")
        x += 1
    
    x = 0
    print()    

