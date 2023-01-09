# Lists
a = [1,2,34,21,12,5,7,18,29,10,7,81,44]
my_newlist = []
n = int(input("Enter the number: "))
for  i in a:
    if i > n:
        my_newlist.append(i)
print(my_newlist)



#  -------OUTPUT--------
# Enter the number: 12
# [34, 21, 18, 29, 81, 44]
#


# Second Method
l1 = [] # Here We creating a new empty list
user = int(input("Enter the number: "))
for i in range(1, user):
    # if i % 2 == 0: # if you want to only even numbers then you will use this condition
    l1.append(i)

print(l1)
my_new_list = [] # Here We creating a new empty list
user_input = int(input("Enter the number: "))
for i in l1:
    if i > user_input:
        my_new_list.append(i)
print(my_new_list)


# -------OUTPUT--------
# Enter the range: 30
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# Enter the number: 23
# [24, 25, 26, 27, 28, 29]



