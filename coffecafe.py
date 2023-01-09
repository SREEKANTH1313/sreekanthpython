print("Welcome to My Coffee Cafe")
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
    user = input("Enter the your favourite item's: ").lower() # Here We Providing two options  for you, you can enter item name or you can enter item nuber.
    quantity = int(input("Enter how many cups you want: "))
    if user == 'tea' or user == '1':
        tea1 = tea1 + quantity * 15
    elif user == 'ginger' or user == '2':
        Ginger1 = Ginger1 + quantity * 20
    elif user == 'boost' or user == '3':
        Boost1 = Boost1 + quantity * 25
    elif user == 'coffee' or user == '4':
        coffee1 = coffee1 + quantity * 20
    user2 = input("Please enter yes/ no if you want another  items: ").lower()
    if user2.lower() == 'no':
        break
total = tea1 + Ginger1 + coffee1 + Boost1
print('your total bill is : ', total)
print('Thank You For Visit My Coffee Cafe')

# -----OUTPUT-----
# Welcome to My Coffee Cafe
# Please choose your favourite item's
# 1: Tea 
# 2: Ginger 
# 3: Boost 
# 4: coffee 
# Enter the your favourite item's: coffee
# Enter how many cups you want: 3
# Please enter yes/ no if you want another  items: yes
# Enter the your favourite item's: ginger
# Enter how many cups you want: 4
# Please enter yes/ no if you want another  items: No
# your total bill is :  140
# Thank You For Visit My Coffee Cafe
