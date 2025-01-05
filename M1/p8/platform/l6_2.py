# # Бесконечное количество имен.
#
# # Напишите программу, которая принимает произвольное количество именованных аргументов и выводит информацию о человеке.
# # Программа должна:
# # Определить функцию print_person_info(**kwargs), которая принимает произвольное количество именованных аргументов.
# # Вывести каждое имя аргумента и его значение.
#
# # Напишите тут ваш код
# def print_person_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_person_info(name="Alice", age=30, city="New York")
#

def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Пример вызова функции
print_person_info(name="John", age=30, city="New York", profession="Engineer")

