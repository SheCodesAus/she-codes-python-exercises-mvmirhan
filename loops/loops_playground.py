# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# for i in range(1,6):  #i is arbitrary variable name
#     print(i)

# for i in range(6):  #0,1,2,3,4,5; range default to zero
#     #i =0, i=1
#     print(i)

# numbers = [10,20,30,40]
# #using for loops
# for number in numbers: #for variable name in list name:
#     print(number)      #print variable name

# for num in range (10): #starts default at zero and does not include the last
#     print(num)

# for num in range(1,11):
#     print(num)

# for num in range(0,13,2): #range(start,stop,skip)
#     print(num)

# for num in range(0,101,5): #range(start,stop,skip)
#     print(num)

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
# # for item in range(len(chilli_wishlist)): #range(4)
# #     # print(item) #0,1,2,3
# #     print(chilli_wishlist[item]) #chilli_wishlist[2]

# for item in chilli_wishlist:
#     print(item)

chilli_wishlist = [              #nested list
["igloo"],
["donut toy", "tennis ball", "crocodile toy"],
["chicken", "peanut butter"],
["cardboard box", "kong", "dig mat"]
]

for category in chilli_wishlist:
    for item in category:
        print(item)

    