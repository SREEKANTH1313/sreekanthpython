pin_chances = 3
# file = open("ATMData.xlsx")
# print(file.read_excelo(PIN))
import pandas as pd
import openpyxl

while pin_chances > 0:
    try:
        import random
        import time
        Balance = random.randint(1000, 100000)
        # file = pd.read_excel("ATMData.xlsx")
        # print(file['PIN'])

        print("Welcome To Axis Bank ATM ")
        time.sleep(1)
        user = (input("Please enter your pin: "))

        # print(len(user))
        if len(user) == 4:
            time.sleep(1)
            print("Please Choose The Below Options.")
            print('''
            1. Check Balance
            2. With Draw Balance
            3. Deposit Money
            4. Clear
            ''')
            print("Your Balance ", Balance)
            options = int(input("Please Choose Correct Option From The Above List: "))
            if options == 1:
                time.sleep(1)
                print("Present Balance in Your Account ", Balance)
                time.sleep(1)
                print("Please Collect Your Card")
                break
            elif options == 2:
                with_draw = int(input("Enter the amount: "))
                if Balance > with_draw:
                    time.sleep(1)
                    print("Collect Your Cash")
                    time.sleep(1)
                    print("Remaining Balance In Your Account ", Balance - with_draw)
                    break

                else:
                    print("Amount is insufficient in Your Account")
            elif options == 3:
                deposit = int(input("Enter the deposit amount: "))
                time.sleep(1)
                updated_amount = Balance + deposit
                time.sleep(1)
                print("Available Balance is ", updated_amount)
                break
            elif options == 4:
                time.sleep(2)
                print("Please Collect Your Card")
                break
            # else:
            #     pin_chances -= 1
            #     print("Incorrect PIN! You have", pin_chances, "chance(s) remaining.")
        else:
            print("Your Entered Incorrect PIN")
            time.sleep(2)
            print("Please Collect Your Card ")
            break

    except TypeError:
        print("Your Pin is not valid and its take only four digits.")
    except ValueError:
        print("It takes only numerical values like(1234) but you entered letters, Please give proper details.")
        break
time.sleep(2)
print("Thank You For Visiting Axis Bank ATM ")










