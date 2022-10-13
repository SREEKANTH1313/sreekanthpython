def sree_12(even):
    print("The even numbers are: ")
    for i in even:
        if i % 2 == 0:
            print(i)


mylist1 = [12, 13, 17, 22, 45, 68, 34, 24, 57, 98]
mylist1.sort()
sree_12(mylist1)


# output
# The even numbers are:
# 12
# 22
# 24
# 34
# 68
# 98
