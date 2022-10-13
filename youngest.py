def mylist_1313(my_list):
    if my_list[0]['age'] < my_list[1]['age']:
        print("name of youngest employee:", my_list[0]['name'])
        print("age of youngest employee:", my_list[0]['age'])
    else:
        print("name of youngest employee:", my_list[1]['name'])
        print("age of youngest employee:", my_list[1]['age'])


list1 = [{"name": "Tina", "age": 30, "birthday": "1990-03-10", "job": "Devops Engineer",
         "address": {"city": "New York", "country": "USA"}},
         {"name": "sree", "age": 25, "birthday": "1995-02-21", "job": "Developer",
         "address": {"city": "Hyderabad", "country": "India"}}]

mylist_1313(list1)

# output
# name of youngest employee: sree
# age of youngest employee: 25
# Process finished with exit code 0
