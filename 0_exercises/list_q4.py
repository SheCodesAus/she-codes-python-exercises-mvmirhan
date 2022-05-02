# Using the following starter code:
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

list_1=[a,b,c]
print(list_1)

#what is the other way to achieve this? 
for i in b:
    a.append(i)
for i in c:
    a.append(i)
print(a)