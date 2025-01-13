# # # # # # # # # # # # # # # if True:
# # # # # # # # # # # # # # #     print("Hello")
# # # # # # # # # # # # # # def example():
# # # # # # # # # # # # # #     print("Hello")
# # # # # # # # # # # # # #      print("World")  # Неправильный отступ вызывает IndentationError
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # example()
# # # # # # # # # # # # #
# # # # # # # # # # # # # def example():
# # # # # # # # # # # # #     eval("if True print('Hello')")  # Неправильный синтаксис вызывает SyntaxError
# # # # # # # # # # # # #
# # # # # # # # # # # # # example()
# # # # # # # # # # # #
# # # # # # # # # # # # try:
# # # # # # # # # # # #     result = 10 / 2
# # # # # # # # # # # # except ZeroDivisionError:
# # # # # # # # # # # #     print("Ошибка: деление на ноль.")
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print(f"Результат: {result}")
# # # # # # # # # # # # finally:
# # # # # # # # # # # #     print("Этот блок выполняется всегда.")
# # # # # # # # # # # try:
# # # # # # # # # # #     file = open("non_existent_file.txt", "r")
# # # # # # # # # # #     content = file.read()
# # # # # # # # # # # except FileNotFoundError:
# # # # # # # # # # #     print("Ошибка: файл не найден.")
# # # # # # # # # # # except IOError:
# # # # # # # # # # #     print("Ошибка: ошибка ввода-вывода.")
# # # # # # # # # # # else:
# # # # # # # # # # #     print(content)
# # # # # # # # # # # finally:
# # # # # # # # # # #     if 'file' in locals() and not file.closed:
# # # # # # # # # # #         file.close()
# # # # # # # # # # #         print("Файл закрыт.")
# # # # # # # # # # a = "1"
# # # # # # # # # # b = 123
# # # # # # # # # # print(locals())
# # # # # # # # #
# # # # # # # # # try:
# # # # # # # # #     # Код, который может вызвать исключение
# # # # # # # # #     result = int("abc")
# # # # # # # # # except (ValueError, ZeroDivisionError) as e:
# # # # # # # # #     print(f"Произошла ошибка: {e}")
# # # # # # # #
# # # # # # # # try:
# # # # # # # #     # Код, который может вызвать NameError
# # # # # # # #     print(undeclared_variable)
# # # # # # # # except NameError as e:
# # # # # # # #     print(f"Произошла ошибка: {e}")
# # # # # # # #     print(f"Тип ошибки: {type(e)}")
# # # # # # #
# # # # # # # try:
# # # # # # #     # Код, который может вызвать ValueError
# # # # # # #     result = int("abc")
# # # # # # # except ValueError as e:
# # # # # # #     print(f"Произошла ошибка: {e}")
# # # # # # #     print(f"Аргументы ошибки: {e.args}")
# # # # # # #     print(f"Сообщение об ошибке: {str(e)}")
# # # # # #
# # # # # # try:
# # # # # #     # Код, который может вызвать несколько типов исключений
# # # # # #     result = 10 / 0
# # # # # # except (ValueError, ZeroDivisionError) as e:
# # # # # #     print(f"Произошла ошибка: {e}")
# # # # # #     print(f"Тип ошибки: {type(e)}")
# # # # # #     print(f"Аргументы ошибки: {e.args}")
# # # # #
# # # # # a = ''
# # # # # int(a)
# # # # # #print(a[0])
# # # #
# # # # try:
# # # #     # Код, который может вызвать исключение
# # # #     result = int(10/0)
# # # # except ValueError as e:
# # # #     exception = e
# # # #     print("Ошибка: некорректное значение.")
# # # # except ZeroDivisionError as e:
# # # #     exception = e
# # # #     print("Ошибка: деление на ноль.")
# # # #
# # # # print(exception)
# # #
# # # def check_number(value):
# # #     if value < 0:
# # #         raise Exception("Sorry, no numbers below zero")
# # #
# # # try:
# # #     check_number(-5)
# # # except Exception as e:
# # #     print(f"Исключение поймано: {e}")
# # #
# # #
# # def check_integer(value):
# #     if not isinstance(value, int):
# #         raise TypeError("Only integers are allowed")
# #
# # try:
# #     check_integer("string")
# # except TypeError as e:
# #     print(f"Исключение поймано: {e}")
# class EmptyVariableError(Exception):
#     pass
#
# def check_non_empty(value):
#     if value == "":
#         raise ValueError("The variable is empty")
#
# try:
#     check_non_empty("")
# except ValueError as e:
#     raise EmptyVariableError("Empty variable detected") from e
