class Student:
    def __init__(self, First_Name, Sur_Name, age, lecturers):
        self.First_Name = First_Name
        self.Sur_Name = Sur_Name
        self.age = age
        self.lecturers = lecturers

    def FullName(self, firstname, lastname):
        print("Full name:", self.First_Name, self.Sur_Name)

    def List_lecturers(self, lecturers):
        print("List of lectures student attend:", self.lecturers)

    def add_lecturers(self, lecturers):
        new_lec = input("Enter the new list of lecturers student attend:  ")
        new_lec1 = new_lec.split(" ")
        for i in new_lec1:
            self.lecturers.append(i)
        print("New lectures list is:", self.lecturers)

    def remove_lecturers(self, lecturers):
        rm_lec = input("Enter list of lecturers to remove:  ")
        self.lecturers.remove(rm_lec)
        print("Subjects list after remove is:", self.lecturers)


first_name = input("Enter first name:  ")
last_name = input("Enter last name:  ")
age = input("Enter age:  ")
lectures = list(input('Enter subject list he/she teaches: ').split(" "))
hello = Student(first_name, last_name, age, lectures)
hello.FullName(first_name, last_name)
hello.List_lecturers(lectures)
hello.add_lecturers(lectures)
hello.remove_lecturers(lectures)


class Professor:
    def __init__(self, firstname, lastname, age, Subject):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.Subject = Subject

    def fullname(self, firstname, lastname):
        print("Full name:", self.firstname, self.lastname)

    def subjects_he_teaches(self, subjects):
        print("List of subjects he teach:", self.Subject)

    def add_subjects(self, subjects):
        new_sub = input("Enter new list of subjects to teach:  ")
        new_sub1 = new_sub.split(" ")
        for i in new_sub1:
            self.Subject.append(i)
        print("New subjects list is:", self.Subject)

    def remove_subjects(self, Subjects):
        remove_sub = input("Enter the list of subjects to remove:  ")
        self.Subject.remove(remove_sub)
        print(" After remove the subjects list is:", self.Subject)


First_name = input("Enter the first name: ")
last_name = input("Enter the last name:  ")
age = input("Enter the  age: ")
subjects = list(input("Enter subject list he/she teaches: ").split(" "))
print(subjects)
hii = Professor(first_name, last_name, age, subjects)
hii.fullname(first_name, last_name)
hii.subjects_he_teaches(subjects)
hii.add_subjects(subjects)
hii.remove_subjects(subjects)


class Lecture:
    def __init__(self, Name, max_no_of_students, Duration, Professor_List):
        self.Name = Name
        self.max_no_of_students = max_no_of_students
        self.duration = Duration
        self.Professor_List = Professor_List

    def name_duration(self, Name, Duration):
        print(" Enter the lecture of name:", self.Name)
        print("Duration of the lecture in minutes is", self.duration)

    def new_professor_add(self, Professor_list):
        new_prof = input("Enter the new list of professors to teach the subjects: ")
        new_prof1 = new_prof.split(" ")
        for i in new_prof1:
            self.Professor_List.append(i)
        print("Old and New professors list is:", self.Professor_List)


name = input("Enter the lecture name: ")
max_students = input("Enter max no,of students: ")
duration = input("Enter the Duration  in minutes: ")
professor_list = list(input('Enter the  professors teach the list of subjects is: ').split(" "))
lec = Lecture(name, max_students, duration, professor_list)
lec.name_duration(name, duration)
lec.new_professor_add(professor_list)


class Person:
    def __init__(self, FirstName, LastName, age):
        self.FirstName = FirstName
        self.LastName = LastName
        self.age = age

    def print_name(self):
        print("Person name is:", self.FirstName, self.LastName)


class Student(Person):
    pass


class Professor(Person):
    pass


first_name = input("Please Enter the student first name: ")
last_name = input("Please Enter the student last  name: ")
age = input("Please Enter the student age: ")
stu_obj = Student(first_name, last_name, age)
stu_obj.print_name()
first_name = input("Please Enter the professor first name: ")
last_name = input("Please Enter the professor last  name: ")
age = input("Please Enter the professor age: ")
prof_obj = Professor(first_name, last_name, age)
prof_obj.print_name()






