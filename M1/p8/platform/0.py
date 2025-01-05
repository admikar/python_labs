# # # # a = [1, 2, 3]
# # # # b = a
# # # # c = [1, 2, 3]
# # # # print(id(a))  # Выводит идентификатор объекта 'a'
# # # # print(id(b))
# # # # print(id(c))
# # #
# # # # # # print(hash("hello"))  # Возвращает хеш-значение строки "hello"
# # # # # # print(hash(42))       # Возвращает хеш-значение числа 42
# # # # # # print(hash((1, 2, 3)))
# # #
# # # # # class MyClass:
# # # # #     def __init__(self):
# # # # #         self.name = "Alice"
# # # # #
# # # # #     def greet(self):
# # # # #         print("Hello, " + self.name)
# # # # #
# # # # # obj = MyClass()
# # # # # print(dir(obj))  # Выводит список атрибутов и методов объекта 'obj'
# # # # # print(dir())
# # # #
# # # # names = ["Alice", "Bob", "Charlie"]
# # # # ages = [25, 30, 35]
# # # # name = ["Alice", "Bob", "Charlie"]
# # # # combined = zip(names, ages, name)
# # # # print(list(combined))
# # # #
# # #
# # # numbers = [1, 2, 3, 4, 5]
# # # print(max(numbers))  # Вывод: 5
# # #
# # # # С ключевой функцией
# # # words = ["apple", "banana", "cherry"]
# # # print(max(words, key=len))  # Вывод: 'banana'
# # #
# # # С ключевой функцией
# # words = ["apple",  "cherry", "banana"]
# # print(max(words))  # Вывод: 'banana'
#
# def infinite_numbers():
#     n = 0
#     while True:
#         yield n
#         n += 1
#
# gen = infinite_numbers()
# print(next(gen))  # 0
# print(next(gen))  # 1

