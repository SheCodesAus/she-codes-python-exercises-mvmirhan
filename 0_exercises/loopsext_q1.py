# Below is a list of foods and their prices per unit:
# Ask the user how many units of each item they bought, then output the corresponding receipt.
# For the input below, assume that the input is provided in the same order as defined in the list above
groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]

#Solution -------------------------------

total_cost=0

for price in range(0,len(groceries)):
    qty=int(input("Enter qty: "))
    unit_cost=float(groceries[price][-1])
    print(f"{qty} x {unit_cost}","=",qty*unit_cost)
    total_cost=total_cost+(qty*unit_cost)
print("Total_cost: $",total_cost)

#CODE THAT DOESNT WORK CORRECTLY LOL!
# qty_spinach = input("Enter qty of spinach: ")
# qty_hot_choco = input("Enter qty of hot choco: ")
# qty_crackers = input("Enter qty of crackers: ")
# qty_bacon = input("Enter qty of bacon: ")
# qty_carrots = input("Enter qty of carrots: ")
# qty_oranges = input("Enter qty of oranges: ")

# qty=[qty_spinach,qty_hot_choco,qty_crackers,qty_bacon,qty_carrots,qty_oranges]
# qty=['1', '3', '2', '1', '4', '2']

# for x in qty:
#     print(x)

# sum=0
# for price in range(0,len(groceries)):     #for price in range(0,6)
#     print(f"{x} x {groceries[price][-1]}"," = ",int(x)*float(groceries[price][-1]))
#     sum=sum+(int(x)*float(groceries[price][-1]))
# print("Total Cost: ",sum)



   


  
     




    


