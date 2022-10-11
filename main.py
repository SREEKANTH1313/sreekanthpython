Employees = [{
  "name": "tina",
  "age": 30,
  "birthday": "1990/03/10",
  "job": "devops engineer",
  "address": {
    "city": "newyork",

    "country": "usa"}},
  {"name": "tim",
   "age": 35,
   "birthday": "1985/02/21",
   "job": "developer",
   "address":
     {"city": "sydney",
      "country": "australia"}}]
n1 = len(Employees)
for n2 in range(n1):
  print(Employees[n2]['name'], Employees[n2]['job'], Employees[n2]['address']['city'])
s = Employees[1]['address']['country']
print("The second employees country is: ", s)
