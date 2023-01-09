# swap case without using swap_case() method.
a = input("Enter the any string: ")
b = ''
for i in a:
    if i.islower():
        b = b + i.upper()
    elif i.isupper():
        b = b + i.lower()
    elif i.isascii():
        b = b + i
print(b)
# ---OutPut---
# Enter the any string: 'sreekanthAlaKuntLA123"Python2."'
# 'SREEKANTHaLAkUNTla123"pYTHON2."'
