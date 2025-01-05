# person_info = {
#     "name": "John Doe",
#     "age": 30,
#     "address": {
#         "street": "123 Main St",
#         "city": "Anytown",
#         "state": "CA",
#         "postal_code": "12345"
#     },
#     "contact": {
#         "email": "john.doe@example.com",
#         "phone": {
#             "home": "555-1234",
#             "work": "555-5678"
#         }
#     }
# }
#
# print(person_info)
#
# def find_key(d, key):
#     if key in d:
#         return d[key]
#     for k, v in d.items():
#         if isinstance(v, dict):
#             result = find_key(v, key)
#             if result:
#                 return result
#     return None
#
# phone = find_key(person_info, "phone")
#
# print(phone)
#
# def change_up_value(d, f_key, f_value):
#     for key, current_value in d.items():
#         if key == f_key:
#             d[key] = f_value
#         elif isinstance(current_value, dict):
#             change_up_value(current_value, f_key, f_value)
#     return d
#
# change_up_value(person_info, "name",  "John Doe 2")
#
# print(person_info)
#
# change_up_value(person_info, "city",  "Nicosia")
#
# print(person_info)
#
# def add_value(d, u_key, f_key , f_value):
#     for key, current_value in d.items():
#         if key == u_key:
#             d[key][f_key] = f_value
#     return d
#
# add_value(person_info, "contact", "whatsup",  "balabol")
#
# print(person_info)
#
# def del_item(d, f_item):
#     for key, value in d.items():
#         if key == f_item or value == f_item:
#             del d[key]
#             return d
#         elif isinstance(value, dict):
#             del_item(value, f_item)
#     return d
#
# del_item(person_info,  "whatsup")
# print(person_info)

# Создаем словарь с информацией о человеке
person = {
    'name': 'Алексей',
    'age': 30,
    'address': {
        'city': 'Москва',
        'street': 'Тверская',
        'house': 10
    },
    'contact_info': {
        'email': 'alexey@example.com',
        'phone': '+7 123 456 7890'
    }
}

# Изменяем значения верхнего уровня
person['name'] = 'Александр'
person['age'] = 31

# Изменяем значения во вложенном словаре
person['address']['city'] = 'Санкт-Петербург'
person['address']['street'] = 'Невский проспект'

# Изменяем значения в более глубоком уровне вложенности
person['contact_info']['email'] = 'alexander@example.com'

# Добавляем новый элемент в вложенный словарь
person['address']['apartment'] = 5

# Удаляем элемент из вложенного словаря
del person['contact_info']['phone']

# Удаляем элемент верхнего уровня
del person['age']

# Выводим результат
print(person)