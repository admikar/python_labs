# ## Генератор выражений.
#
# # Напишите программу, которая использует генераторное выражение для создания
# # последовательности квадратов чисел от 1 до 10. Программа должна:
# # Создать генераторное выражение для генерации квадратов чисел.
# # Использовать этот генератор для вывода всех значений последовательности.
#
# # Напишите тут ваш код

# # def squears():
# #     for i in range(10):
# #         yield i ** 2
# #
# # squea = squears()
# #
# # for value in squea:
# #     print(value)
#
# squea = (i ** 2 for i in range(1, 11))
#
# for value in squea:
#     print(value)
#
#
#
# Генераторное выражение для квадратов чисел от 1 до 10
squares = (x**2 for x in range(1, 11))

# Вывод всех значений последовательности
for square in squares:
    print(square)