
print(" Below is a list of foods and their prices per unit: Ask the user how many units of each item they bought, then output the corresponding receipt. For the input below, assume that the input is provided in the same order as defined in the list above")

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
spinach = 0
receipt=[]

for price in range(0,len(groceries)):
    qty=int(input("Enter qty: "))
    unit_cost=float(groceries[price][-1])
    item=groceries[price][0], round(qty*unit_cost,2)
    receipt.append(item)   
    total_cost=total_cost+(qty*unit_cost)

print("===Izzy's Food Emporium===")
for i in range(0,len(receipt)):
    print(receipt[i][0],"      $",receipt[i][-1])
print("=================================")
print("Total_cost: $",round(total_cost,2))



# print(receipt[0][0],"   ",receipt[0][-1])
# print(receipt[1][0],"   ",receipt[1][-1])
# print(receipt[2][0],"   ",receipt[2][-1])
# print(receipt[3][0],"   ",receipt[3][-1])
# print(receipt[4][0],"   ",receipt[4][-1])
# print(receipt[5][0],"   ",receipt[5][-1])














