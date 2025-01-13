# # Использование traceback
#
# # Напишите функцию divide_numbers, которая принимает два аргумента и делит первое число на второе.
# # Если возникает исключение ZeroDivisionError, перехватите его и выведите стек-трейс, используя модуль traceback.
#
# # Напишите тут ваш код
# import traceback
# def divide_numbers(f_digit, s_digit):
#     try:
#         return f_digit / s_digit
#     except ZeroDivisionError:
#         traceback.print_exc()
#
# divide_numbers(0, 1)
#

import traceback

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        traceback.print_exc()

# Пример вызова функции
divide_numbers(10, 0)

