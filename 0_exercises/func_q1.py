print("Q1:Write a function that takes a temperature in fahrenheit and returns the temperature in celsius.")
print("==============================================================================================")

temp_F=(input("Write a temperature in F: "))

def conv_F_C(temp_F):
    temp_C = (float(temp_F) - 32) * (5/9)
    return  round(temp_C,2)
print(conv_F_C(temp_F))
