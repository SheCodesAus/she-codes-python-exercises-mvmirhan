# But Roary can’t actually get the moths by herself!
# Amend the previous program to determine whether or not it is time for Roary to go moth hunting.
# Variable Value Output
# moths_in_house = True and mitch_is_home = True then Hoooman! Help me get the moths!
# moths_in_house = False and mitch_is_home = False then No threats detected.
# moths_in_house = True and mitch_is_home = False then Meooooooooooooow! Hissssss!
# moths_in_house = False and mitch_is_home = True then Climb on Mitch.

moths_in_house = False
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print ("Hoooman! Help me get the moths!")
elif not(moths_in_house) and not(mitch_is_home): # not (moths_in_house = True and mitch_is_home = True)
    print ("No threats detected.")
elif moths_in_house and not(mitch_is_home):
    print ("Meooooooooooooow! Hissssss!")
else:
    print ("Climb on Mitch.")


