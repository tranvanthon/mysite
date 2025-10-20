"""class Student:
    id = ""
    name = ""

    def add(self, id, name):
        self.id = id
        self.name = name

    def show_student(self):
        print(f"Name:  {self.name} id:  {self.id}")


# Callback

a = Student()
a.add("001", "Thon")
a.show_student()
"""


# Ham khoi tao __init__():
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Yourname is: {self.name} \nYourage is: {self.age}")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


name = input("Please enter name: ")
age = input("Please enter age: ")

p = Person.set_name(name, age)

p.show()
