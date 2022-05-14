print("Q1:Write a function that takes a temperature in fahrenheit and returns the temperature in celsius.")

temp_F=int(input("Write a temperature in F: "))

def conv_F_C(temp_F):
    temp_C = (temp_F - 32) * (5/9)
    return  temp_C
print(conv_F_C(temp_F))