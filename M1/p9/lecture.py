# # class Cat:
# #     def eat(self):
# #         print("Eating")
# #boris = Cat()
# #boris.high = 30
# #print(boris.high)
# #print(boris)
# import random
#
# from numpy.f2py.crackfortran import publicpattern
#
#
# class Cat:
#     ### danter metods or magical metods with __
#     def __init__(self, name, age, height, color="black"):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.color = color
#         self._number = random.randint(1, 100) ## _ mean protected
#         self._number_2 = random.randint(1, 100) ## __ mean privet
#
#     ### self it's link on myself )
#     def eat(self):
#         print(f"{self.name} Eating")
#
# boris = Cat("Boris", 10, 100)
#
# print(boris.eat())
# print(boris.color)
#
#
# # Nasledovanie
# class Lion(Cat):
#     def get_sound_r(self):
#         print("RRR")
#
#
# # Abstraction
# create only needed function, Abstraction from other things (minimum)
#
#
# # incopsulyaciya
# socritie i sohranenie dannih
# public(default)
# privet(only inside class)
# protected(can share with sub classes)
#
# self._number = random.randint(1, 100)  ## _ mean protected
# self._number_2 = random.randint(1, 100)  ## __ mean privet
#
# # polimorfizm
# can use common function for different type of data

class Student:
    def __init__(self, first_name, last_name, numbers):
        self.first_name = first_name
        self.last_name = last_name
        self.numbers = numbers

    def __repr__(self):
        return self.first_name


student_1 = Student(first_name="A", last_name="A", numbers=[1, 2, 3, 4, 5])
student_2 = Student(first_name="B", last_name="B", numbers=[6, 7, 8, 9, 10])

list_students = [
    student_1,
    student_2
]

for student in list_students:
    sum_number = sum(student.numbers)
    student.average = sum_number / len(student.numbers)

tmp = sorted(list_students, key=lambda x: x.average)
print(tmp)