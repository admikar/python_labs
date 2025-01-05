# # Генератор.
#
# # Напишите программу, которая создает функцию-генератор счетчика с использованием замыканий.
# # Программа должна:
# # Определить внешнюю функцию make_counter(), которая создает и возвращает внутреннюю функцию counter().
# # Внутренняя функция counter() должна увеличивать значение счетчика и возвращать его.
# # Создать несколько независимых счетчиков и вызвать их несколько раз, выводя результат на экран.
#
# # Напишите тут ваш код
# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
#
# a1 = make_counter()
# a2 = make_counter()
#
# print(a1())
# print(a2())
#
# print(a1())
# print(a2())
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

# Создание независимых счетчиков
counter1 = make_counter()
counter2 = make_counter()

# Вызов счетчиков и вывод результата на экран
print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1
print(counter1())  # 3
print(counter2())  # 2