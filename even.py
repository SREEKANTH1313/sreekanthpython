def sree_12():
    
    even = []
    odd = []

    for i in mylist1:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print("The Even Number List is: ", even)
    print("The Odd Number List is: ", odd)


mylist1 = [12, 13, 17, 22, 45, 68, 34, 24, 57, 98]
mylist1.sort()
sree_12()


# output
# The Even Number List is:  [12, 22, 24, 34, 68, 98]
# The Odd Number List is:  [13, 17, 45, 57]
