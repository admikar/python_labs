# # Три способа порыться в словаре.
#
# # Напишите программу, которая создает словарь с информацией о человеке.
# # Программа должна:
# # Получить значение по ключу с использованием квадратных скобок.
# # Безопасно получить значение по ключу с использованием метода get().
# # Использовать метод setdefault() для получения значения по ключу и добавления ключа, если он отсутствует.
#
# # Напишите тут ваш код
#
# person = {"name": "Alice", "age": 25, "city": "New York"}
#
# print(person['name'])
# print(person.get('name'))
#
# city = person.setdefault("city2", "New York")
#
# print(city)
# print(person)
# Создание словаря с информацией о человеке
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Получение значения по ключу с использованием квадратных скобок
name = person['name']
print(f'Name: {name}')

# Безопасное получение значения по ключу с использованием метода get()
age = person.get('age')
print(f'Age: {age}')

# Использование метода setdefault() для получения значения по ключу и добавления ключа, если он отсутствует
country = person.setdefault('country', 'USA')
print(f'Country: {country}')

# Вывод всего словаря, чтобы увидеть изменения
print(person)