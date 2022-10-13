def sree_13(myname):
    s1_count = 0
    s2_count = 0
    for m in myname:
        if m.isupper():
            s1_count += 1
        elif m.islower():
            s2_count += 1
    print("The uppercase letters is: ", s1_count)
    print("The lowercase letters is: ", s2_count)


hello = input("Enter any one character name: ")
sree_13(hello)

# output
# Enter any one character name: Hello SREEkanth
# The uppercase letters is:  5
# The lowercase letters is:  9
#
# Process finished with exit code 0



