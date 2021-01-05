from operator import attrgetter


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Person name is {self.name} and age is {self.age}'.format(self=self)


class Classroom:
    def __init__(self):
        self.list_of_students = []

    def add_student(self, name, age):
        self.list_of_students.append(Student(name, age))

    def oldest_student(self):
        return max(self.list_of_students, key=attrgetter('age'))

