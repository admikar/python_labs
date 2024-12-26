# student = {"name": "Alice", "age": 25, "university": "MFTI"}
#
# for index, (key, value) in enumerate(student.items()):
#     print(index, key, value)

# Создаем словарь с информацией о студенте
student_info = {
    'name': 'Alice',
    'age': 21,
    'university': 'Harvard'
}

# Перебираем пары ключ-значение словаря с использованием функции enumerate
for index, (key, value) in enumerate(student_info.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")

