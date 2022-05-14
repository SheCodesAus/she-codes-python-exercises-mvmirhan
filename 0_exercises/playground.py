#Find the minimum value
numbers = [4,7,10,1,2]
min_value = numbers[0]
min_location = 0
index = 0

for num in numbers:
    if num < min_value:
        min_value = num
        min_location = index
    index += 1    
print(min_value,min_location)

    # print(f"Min value: {min_value}, num: {numbers}")

