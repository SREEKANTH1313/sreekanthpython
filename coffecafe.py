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

# QR  Code
# import pyqrcode
# import qrcode
# # # from pyzbar import decode
# # # from PIL
# # import image
# q = qrcode.QRCode(version=1, box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_L, border=5)
# q.add_data('b')
# a = pyqrcode.create('Welcome to  My  Coffee Cafe')
# a.png('Mycode.png', scale=8)
# # b = qrcode.make('https://forms.gle/7px5fiJWqeJzfGno8')
# b = qrcode.make('https://forms.gle/GcnDL5sGKD1MaT1h6')
# b.save('Mycode.png')
#

