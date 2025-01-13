# # Обработка исключений.
#
# # Напишите функцию safe_division, которая принимает два числа и выполняет их деление.
# # Обработайте исключения, которые могут возникнуть при делении на ноль
# # и при передаче некорректных значений (например, строки вместо чисел).
# # Функция должна возвращать сообщение об ошибке или результат деления.
#
# # Напишите тут ваш код
# def safe_division(f_digit, s_digit):
#     try:
#         result = f_digit / s_digit
#     except ZeroDivisionError:
#         result = "Ошибка: деление на ноль."
#     except TypeError:
#         result = "Ошибка: некорректное значение."
#     finally:
#         return result
#
# print(safe_division(2, "a"))

def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    except TypeError:
        return "Ошибка: некорректный тип данных"
    return result

