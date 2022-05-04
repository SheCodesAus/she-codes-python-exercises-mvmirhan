#Method 1: Given a list, use a for loop to sum all the numbers in the list

random_numbers = [3, 5, 9, 1]   # initialize a list of integers
total = 0                       # initialize variable to hold the sum of list elements
for num in random_numbers:      # iterate over the list   
    total = total + num         # add current list element to the sum
print(total)

random_numbers = [-3, -5, 9, 1]  
total = 0                       
for num in random_numbers:        
    total = total + num         
print(total)

random_numbers = []  
total = 0                       
for num in random_numbers:        
    total = total + num         
print(total)

#Method 2: Given a list, use a for loop to sum all the numbers in the list

random_numbers_1 = [3, 5, 9, 1]
random_numbers_2 = [-3, -5, 9, 1]
random_numbers_3 = [] 

sumlist = sum(random_numbers_1)
sumlist1 = sum(random_numbers_2)
sumlist2 = sum(random_numbers_3)

print(f"{sumlist}")
print(f"{sumlist1}")
print(f"{sumlist2}")


