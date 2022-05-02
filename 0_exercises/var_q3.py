# Write a program that takes a distance in kilometers from the user, 
# and output the distance in meters and centimeters.

a=float(input("How many kilometres? "))
print(a,"km = ",int(a*1000),"m")
print(a,"km = ",int(a*100000),"cm")

