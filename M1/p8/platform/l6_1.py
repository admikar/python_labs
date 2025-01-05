# # Бесконечность не предел.
#
# # Напишите программу, которая принимает произвольное количество чисел и выводит их сумму.
# # Программа должна:
# # Определить функцию sum_numbers(*args), которая принимает произвольное количество чисел.
# # Вычислить сумму всех переданных чисел.
# # Вывести результат.
#
# # Напишите тут ваш код
# def sum_numbers(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
#
# summa = sum_numbers(1, 2, 3, 4, 5)
#
# print(summa)

def sum_numbers(*args):
    return sum(args)

# Example usage:
numbers = [1, 2, 3, 4, 5]
print(sum_numbers(*numbers))  # Output: 15

# You can also pass the numbers directly:
print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15