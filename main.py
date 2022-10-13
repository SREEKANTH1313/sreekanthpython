loop = 0
loop = 1
count = 0
while loop == 1:
    print(" Hey user your options are Here:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo Division")
    operation = input("Hello user choose  anyone operation: ")
    try:
        if operation == '1':
             n1 = int(input("Enter the First Number: "))
             n2 = int(input("Enter the Second Number: "))
             print(n1, "+", n2, "=", n1 + n2)
             count += 1
        elif operation == '2':
             num1 = int(input("Enter the First Number: "))
             num2 = int(input("Enter the Second Number:"))
             print(num1, "-", num2, "=", num1 - num2)
             count += 1
        elif operation == '3':
            m1 = int(input("Enter the First Number: "))
            m2 = int(input("Enter the Second Number: "))
            print(m1, "x", m2, "=", m1 * m2)
            count += 1
        elif operation == '4':
            d1 = int(input("Enter the First Number: "))
            d2 = int(input("Enter the Second Number: "))
            print(d1, "/", d2, "=", d1 / d2)
            count += 1

        elif operation == '5':
            p1 = int(input("Enter the First Number: "))
            p2 = int(input("Enter the Second Number: "))
            print(p1, "%", p2, "=", p1 % p2)
            count += 1

        elif operation == 'exit':
            loop = 0
            print("The number of operations user did:", count)
        else:
            print("%d is not valid input. Please enter the correct option." % operation)
    except Exception:
        print("Hey  User you Cannot divide by zero!, please try again")
    except ValueError and TypeError:
        print("%r is not valid input.  Please enter 1, 2, 3, 4." % operation)


# output

# Hey user your options are Here:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulo Division
# Hello user choose  anyone operation: 1
# Enter the First Number: 12
# Enter the Second Number: 13
# 12 + 13 = 25
#  Hey user your options are Here:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulo Division
# Hello user choose  anyone operation: 2
# Enter the First Number: 13
# Enter the Second Number:2
# 13 - 2 = 11
#  Hey user your options are Here:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulo Division
# Hello user choose  anyone operation: 3
# Enter the First Number: 12
# Enter the Second Number: 13
# 12 x 13 = 156
#  Hey user your options are Here:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulo Division
# Hello user choose  anyone operation: 4
# Enter the First Number: 13
# Enter the Second Number: 0
# Hey  User you Cannot divide by zero!, please try again
#  Hey user your options are Here:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulo Division
# Hello user choose  anyone operation: 4
# Enter the First Number: 14
# Enter the Second Number: 2
# 14 / 2 = 7.0
#  Hey user your options are Here:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulo Division
# Hello user choose  anyone operation: 5
# Enter the First Number: 14
# Enter the Second Number: 2
# 14 % 2 = 0
#  Hey user your options are Here:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulo Division
# Hello user choose  anyone operation: exit
# The number of operations user did: 5
#
# Process finished with exit code 0
#


