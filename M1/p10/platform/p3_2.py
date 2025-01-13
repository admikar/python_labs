# # Извлечение информации из исключения
#
# # Напишите функцию read_integer, которая принимает строку и пытается преобразовать её в целое число.
# # Если возникает ValueError, обработайте исключение и выведите аргументы ошибки и тип ошибки.
# # Дополнительно, сохраните исключение в переменной и выведите её за пределами блока except.
#
# # Напишите тут ваш код
#
#
# def read_integer(f_string):
#     exception = None
#     try:
#         int(f_string)
#     except ValueError as e:
#         exception = e
#         print(f"Аргументы ошибки: {e.args}")
#         print(f"Тип ошибки: {type(e)}")
#     print(exception)
#
# read_integer("abc")

def read_integer(input_string):
    exception_instance = None
    try:
        return int(input_string)
    except ValueError as e:
        exception_instance = e
        print(f"Error arguments: {e.args}")
        print(f"Error type: {type(e)}")
    print(f"Exception instance: {exception_instance}")

# Пример вызова функции
read_integer("abc")