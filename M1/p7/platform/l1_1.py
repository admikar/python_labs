# # Проверка на пустоту.
#
# # Напишите программу, которая создает несколько словарей с различным количеством элементов.
# # Программа должна:
# # Вывести количество элементов в каждом словаре.
# # Проверить, пустой ли каждый словарь, и вывести соответствующее сообщение.
# # Для проверки пустоты словаря нужно создать функцию check_empty
#
# # Напишите тут ваш код
# person = {"name": "Alice", "age": 25, "city": "New York"}
# person1 = {"name": "Alice", "age": 25}
# person2 = dict()
#
# print(len(person))
# print(len(person1))
# print(len(person2))
#
# def check_empty(checker):
#     if len(checker) == 0:
#         return True
#     return False
#
# print(check_empty(person))
# print(check_empty(person1))
# print(check_empty(person2))

def check_empty(d):
    return len(d) == 0

# Создаем несколько словарей с различным количеством элементов
dict1 = {}
dict2 = {'a': 1, 'b': 2}
dict3 = {'x': 10}
dict4 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

dictionaries = [dict1, dict2, dict3, dict4]

# Выводим количество элементов в каждом словаре и проверяем их на пустоту
for i, d in enumerate(dictionaries, 1):
    print(f"Словарь {i}: {len(d)} элементов")
    if check_empty(d):
        print(f"Словарь {i} пустой")
    else:
        print(f"Словарь {i} не пустой")