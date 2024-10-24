# #from collections import OrderedDict
# В базе данных магазина вся необходимая информация по товарам делится на два словаря: первый отвечает за коды товаров, второй — за списки количества разнообразных товаров на складе:
# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
#  
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520},
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }
#  
# Каждая запись второго словаря отображает, сколько и по какой цене закупалось товаров (цена указана за 1 шт.).
# Напишите программу, которая рассчитывает, на какую сумму лежит каждого товара на складе, и выводит эту информацию на экран.
# б

goods = {
'Лампа': '12345',
'Стол': '23456',
'Диван': '34567',
'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

#good = input("Insert name goods: ")
#code = goods.get(good)
#m_list = store.get(code)
price = 0
quantity = 0
result = 0
total_quantity = 0
for key, value in goods.items():
    m_list = store.get(value)
    for m_dict in m_list:
        quantity += m_dict.get("quantity")
        total_quantity += quantity
        price += m_dict.get("price")
        result += quantity * price
    print(f"{key} - {total_quantity} шт, price {result}")
    price = 0
    quantity = 0
    result = 0
    total_quantity = 0
