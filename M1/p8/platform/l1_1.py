# # Лямбда в квадрате.
#
# # Напишите программу, которая использует лямбда-функцию для возведения в квадрат
# # каждого элемента списка чисел с использованием функции map(). Программа должна:
# # Создать список чисел.
# # Использовать map() и лямбда-функцию для возведения каждого числа в квадрат.
# # Вывести результат.
#
# # Напишите тут ваш код
# a = list([1,2,3])
# ax2 = list(map(lambda x: x ** 2, a))
# print(ax2)
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

