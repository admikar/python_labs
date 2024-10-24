# # person1 = {"name": "John", "age": 30, "city": "New York"}
# # person2 = dict([("name", "John"), ("age", 30), ("city", "New York")])
# # person3 = dict(name="John", age=30, city="New York")
# #
# # print(person1)
# # print(person2)
# # print(person3)
#
# people_1 = {"name": "John", "age": 30, "city": "New York"}
#
# people_2 = dict([("name", "John"), ("age", 30), ("city", "New York")])
#
# people_3 = dict(name="John", age=30, city="New York")
#
# print(people_1)
#
# print(people_2)
#
# print(people_3)
# Использование фигурных скобок {}
person1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Использование функции dict() с последовательностью пар ключ-значение
person2 = dict([("name", "Bob"), ("age", 25), ("city", "Los Angeles")])

# Использование функции dict() с именованными аргументами
person3 = dict(name="Charlie", age=35, city="Chicago")

# Вывод всех трех словарей
print(person1)
print(person2)
print(person3)