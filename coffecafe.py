print("Welcome to Our Coffee Cafe")
print("Please choose your favourite item's")
print('1: ' 'Tea ')
print('2: ' 'Ginger ')
print('3: ' 'Boost ')
print('4: ' 'coffee ')
coffee1 = 0
Ginger1 = 0
Boost1 = 0
tea1 = 0
while True:
    user = input("Enter the your favourite item's: ").lower()
    quantity = int(input("Enter how many cups you want: "))
    if user == 'tea' or user == '1':
        tea1 = tea1 + quantity * 15
        # print('Your Tea Bill is : ', tea1)
    elif user == 'ginger' or user == '2':
        Ginger1 = Ginger1 + quantity * 20
        # print('Your Ginger Bill is : ', int(Ginger1))
    elif user == 'boost' or user == '3':
        Boost1 = Boost1 + quantity * 25
        # print('Your  Boost Bill is : ', Boost1)
    elif user == 'coffee' or user == '4':
        coffee1 = coffee1 + quantity * 20
        # print('Your Coffee Bill is : ', coffee1)
    user2 = input("Please enter yes/ no if you want another  items: ").lower()
    if user2.lower() == 'no':
        break
total = tea1 + Ginger1 + coffee1 + Boost1
print('your total bill is : ', total)
