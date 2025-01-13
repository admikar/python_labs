# # Получение числа.
#
# # Напишите функцию process_input, которая принимает строку и пытается преобразовать её в целое число.
# # Если преобразование успешно, функция должна возвращать квадрат числа.
# # Если строка не является числом, обработайте ValueError и выведите сообщение об ошибке.
# # Если строка пустая, обработайте IndexError и выведите соответствующее сообщение.
#
# # Напишите тут ваш код
# def process_input(f_string):
#     try:
#         if not f_string:
#             raise IndexError()
#         f_digit = int(f_string)
#     except ValueError:
#         return "Ошибка: некорректный тип данных"
#     except IndexError:
#         return "Ошибка: пустых данных"
#     else:
#         return f_digit ** 2
#
#
# # Примеры вызова функции
# print(process_input("5"))  # Вывод: 25
# print(process_input("abc"))  # Вывод: Ошибка: введенная строка не является числом.
# print(process_input(""))  # Вывод: Ошибка: введена пустая строка.
#

def process_input(input_string):
    try:
        if input_string == "":
            raise IndexError("Пустая строка")
        number = int(input_string)
        return number ** 2
    except ValueError:
        print("Ошибка: введенная строка не является числом.")
    except IndexError:
        print("Ошибка: введена пустая строка.")

# Примеры вызова функции
print(process_input("5"))         # Вывод: 25
print(process_input("abc"))       # Вывод: Ошибка: введенная строка не является числом.
print(process_input(""))          # Вывод: Ошибка: введена пустая строка.