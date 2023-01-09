# Lists
a = [1,2,34,21,12,5,7,18,29,10,7,81,44]
my_newlist = []
n = int(input("Enter the number: "))
for  i in a:
    if i > n:
        my_newlist.append(i)
print(my_newlist)