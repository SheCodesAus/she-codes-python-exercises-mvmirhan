# Lists
# 3 elements
# 0 index, 0,1,2
# characters = ["a","b","c"]
# print(characters[2])
# print(characters)  #['a', 'b', 'c']
# print(type(characters))
# characters.append("d")  #to add only 1 item
# characters.extend(["e","f"])  #to add multiple items
# characters.insert(1,"g") #['a', 'g', 'b', 'c', 'd', 'e', 'f']; inserts before the index specified (i.e. 1)
# print(characters[-1])
# print(characters[-2])
# print(characters[0:2]) #starting index (i.e. 0) included, and excluded the stopping element (i.e. 2)
# print(characters[1:3]) #starting index (i.e. 0) included, and excluded the stopping element (i.e. 2)
# print(characters) #['a', 'b', 'c', 'd']
# print(characters.pop(2))
# print(characters.remove("a"))
# print(characters)

chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
# print(chilli_wishlist)
# print(chilli_wishlist[2])
# print(chilli_wishlist[-1])
# print(chilli_wishlist[3])
# print(chilli_wishlist[1:3])

# chilli_wishlist[1] = "carrot" #over-write index specified
# print(chilli_wishlist)

# print(chilli_wishlist[1:4])
# print(chilli_wishlist[1:4:1])
# print(chilli_wishlist[1:4:2]) #The last number specific the interval you want to skip from the index

#Print the sublist of items positions 2 though to 3
#Print the items in the -3 position
  
# print(chilli_wishlist[2:4])
# print(chilli_wishlist[-3])

# print(chilli_wishlist.extend(['kong', 'tennis ball', 'crocodile toy']))
# print(chilli_wishlist.append(['kong', 'tennis ball', 'crocodile toy']))
# print(chilli_wishlist)

# chilli_wishlist.pop(2)
# chilli_wishlist.remove("igloo")
# print(chilli_wishlist)

characters = ["a","b","c"]
print(characters)
if "d" in characters:
    print("Good")
else: characters.append("d")
print(characters)






