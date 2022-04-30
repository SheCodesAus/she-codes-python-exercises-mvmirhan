# Write a program that implements the algorithm for Red Light Cameras.
# Variable Value Output
# light_colour = "Red" and car_detected = False then Do nothing.
# light_colour = "Red" and car_detected = True then Flash!
# light_colour = "Green" and car_detected = False then Do nothing.
# light_colour = "Green" and car_detected = True then Do nothing.
# light_colour = "Amber" and car_detected = False then Do nothing.
# light_colour = "Amber" and car_detected = True then Do nothing


light_color = "Green"
car_detected = True

if light_color == "Red" and car_detected:
    print("Flash")
else:
    print("Do Nothing")

