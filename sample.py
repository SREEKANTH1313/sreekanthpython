my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
new_list = []
number = []
for i in my_list:
    if i >=10:
        new_list.append(i)
print(new_list)
user_input = int(input("enter the number : "))
for numb in my_list:
    if numb > user_input:
        number.append(numb)
print(number)
