
loop = 1
count = 0
choice = 0
while loop == 1:
    print(" Hey user your options are Here, please choose anyone:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Hello user choose your option: ")
    try:
        if choice == '1':
             n1 = int(input("Enter the First Number: "))
             n2 = int(input("Enter the Second Number: "))
             print(n1, "+", n2, "=", n1 + n2)
             count += 1
        elif choice == '2':
             num1 = int(input("Enter the First Number: "))
             num2 = int(input("Enter the Second Number:"))
             print(num1, "-", num2, "=", num1 - num2)
             count += 1
        elif choice == '3':
            m1 = int(input("Enter the First Number: "))
            m2 = int(input("Enter the Second Number: "))
            print(m1, "x", m2, "=", m1 * m2)
            count += 1
        elif choice == '4':
            d1 = int(input("Enter the First Number: "))
            d2 = int(input("Enter the Second Number: "))
            print(d1, "/", d2, "=", d1 / d2)
            count += 1
        elif choice == 'exit':
             loop = 0
        else:
            print("%d is not valid input. Please enter the correct option." % choice)
    except ValueError and TypeError:
        print("%r is not valid input.  Please enter 1, 2, 3, 4." % choice)
    print("The number of calculations user did:", count)


