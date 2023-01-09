employee ={
    'name': 'Tim',
    'age': 30,
    'birthday': "1990-03-10",
    'job': 'DevOps Engineer'
}
employee['job'] = 'Software Engineer'
employee.__delitem__('age')
for key, value in employee.items():
    print(key, ' : ', value)

#     ---OutPut---
#     name  :  Tim
#     birthday  :  1990-03-10
#     job  :  Software Engineer
