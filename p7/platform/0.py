# # # # # # # # # # Создание пустого словаря
# # # # # # # # # empty_dict = {}
# # # # # # # # #
# # # # # # # # # # Создание множества с элементами
# # # # # # # # # unique_items = {
# # # # # # # # #     "name",
# # # # # # # # #     "age",
# # # # # # # # #     "city"
# # # # # # # # # }
# # # # # # # # # print(type(unique_items))
# # # # # # # # # print(unique_items)
# # # # # # # #
# # # # # # # # # Создание словаря с ключами и значением по умолчанию
# # # # # # # # keys = ["name", "age", "city"]
# # # # # # # # default_value = None
# # # # # # # # person = dict.fromkeys(keys, default_value)
# # # # # # # # print(person)
# # # # # # # #
# # # # # # # # Создание словаря из переменных
# # # # # # # name = "John"
# # # # # # # age = 30
# # # # # # # city = "New York"
# # # # # # #
# # # # # # # person = {"name": name, "age": age, "city": city}
# # # # # # # print(person)
# # # # # # # Создание словаря с помощью генератора словаря
# # # # # # squares = {x: x**2 for x in range(1, 6)}
# # # # # # print(squares)
# # # # # # Обращение к значениям в словаре
# # # # # person = {"name": "John", "age": 30, "city": "New York"}
# # # # # print(person["name"])  # Выведет: John
# # # # # Использование метода get() для обращения к значениям в словаре
# # # # person = {"name": "John", "age": 30, "city": "New York"}
# # # # print(person.get("name"))  # Выведет: John
# # # # print(person.get("address", "Адрес не найден"))  # Выведет: Адрес не найден
# # # # print(person.get("address"))
# # # person = {"name": "Alice", "age": 25, "city": "New York"}
# # # values_set = set(person.values())
# # # print(values_set)
# # person = {"name": "Alice", "age": 25}
# # person.setdefault("city", "New York")
# # print(person)
# # city = person.setdefault("city", "New")
# # print(city)
# # print(person)
#
# person = {"name": "Alice", "age": 25, "city": "New York"}
# age = person.pop("ages", 12)
# print(age)

