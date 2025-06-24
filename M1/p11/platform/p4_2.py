# # Итератор для коллекции
#
# # Напишите класс CollectionIterator, который будет итерироваться по произвольной коллекции (список, строка и т.д.).
# # Реализуйте методы __iter__ и __next__.
#
# # Напишите тут ваш код
# class CollectionIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         item = self.data[self.index]
#         self.index += 1
#         return item
#
# # Использование
# my_iterable = CollectionIterator("test")
# for item in my_iterable:
#     print(item)

class CollectionIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.collection):
            item = self.collection[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

# Примеры использования:
# Для списка
ci_list = CollectionIterator([1, 2, 3, 4])
for item in ci_list:
    print(item)

# Для строки
ci_string = CollectionIterator("hello")
for char in ci_string:
    print(char)