#Data Types - String, Integer, Floats, Boolean
#Boolean can only take two values, True or False (case sensitive)
#Boolean Operators - NOT, AND, OR

# b1 = True
# b2 = False
# # print(type(b1))

# knows_password = True
# knows_username = False
# login = knows_password and knows_username
# print(type(login))
# print(not knows_password)

# recover = knows_password or knows_username


# is_raining = True
# is_cold = True
# print(type(is_raining))
# type(is_cold)
# print (not is_raining)
# print (is_raining and is_cold)
# print (is_raining and not is_cold)

# print(is_raining)
# print(not is_raining)

# Comparison Operators
# == Equal
# != Not Equal
# > Greater than
# < Less than


# print (10 > 5) #True
# print (1 > 1.5) #False
# print (5.9 != 5.8) #True

# print ("Asli" == "Georgie") #False
# print ("Asli" == "asli") #False
# #False because upper case is considered another integer to its equivalent lower case

# print (3 == 3.0) #True
# print (type(3) == type(3.0)) #False

# temperature = 16
# print (temperature < 18) #True
# wind_chill = 3
# print (wind_chill > 4) #False
# print (temperature - wind_chill < 16)

# name = "Hayley"
# print("hayley" == name) #False
# print("Hayley" == name) #True

# if 5 > 4:
#     print ("Hello")

# name = "Camilla"
# if name == "Asli":
#     print("Hello again")
# elif name == "Camilla": #wrapping another if inside an if 
#     print(f"Hello {name}, what are we doing today?")
# else:
#     print("WOW HELLO I MISSED YOU")

is_raining = False
temperature = 16
wind_chill = 3

# if is_raining:
#     print("Take an umbrella!")
# else:
#     print("Do not take an umbrella")

# if temperature - wind_chill < 16:
#     print ("Take a jumper")
# elif temperature - wind_chill > 30:
#     print ("Euck, it's hot today, stay home")
# else:
#     print("wow, what a lovely day")

if temperature - wind_chill < 16 and is_raining:
    print ("Just stay home.")
else:
    if True:
        print("You'll need an umbrella today")
    elif temperature - wind_chill < 16:      #computer will only compile if previous if is false
        print("You'll need a jumper today")

if temperature - wind_chill < 16 and is_raining:
    print ("Just stay home.")
else:
    if True:
        print("You'll need an umbrella today")
    if temperature - wind_chill < 16:        #computer will compile all if statement
        print("You'll need a jumper today")













