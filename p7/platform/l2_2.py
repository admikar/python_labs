# # Отображение пар.
#
# # Напишите программу, которая создает словарь с информацией о продукте (например, название, цена, количество).
# # Программа должна:
# # Вывести все пары ключ-значение с использованием метода items().
# # Итерировать по всем парам ключ-значение и вывести их на экран.
# # Добавить новую пару ключ-значение в словарь и снова вывести все пары ключ-значение.
#
# # Напишите тут ваш код
#
# def print_dict(d):
#     for key, value in d.items():
#         print(f"{key}: {value}")
#
# product = {
#     "name": "Apple",
#     "price": 1,
#     "count": 1000
# }
#
# print_dict(product)
# product["waranty"] = 1
# print_dict(product)
# Создаем словарь с информацией о продукте
product_info = {
    'Название': 'Помидоры',
    'Цена': 50,
    'Количество': 100
}

# Выводим все пары ключ-значение с использованием метода items()
for key, value in product_info.items():
    print(f"{key}: {value}")

print("\n")

# Итерируем по всем парам ключ-значение и выводим их на экран
for key, value in product_info.items():
    print(f"{key}: {value}")

print("\n")

# Добавляем новую пару ключ-значение в словарь
product_info['Цвет'] = 'Красный'

# Снова выводим все пары ключ-значение
for key, value in product_info.items():
    print(f"{key}: {value}")