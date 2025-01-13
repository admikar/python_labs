# # Анализ стек-трейс
#
# # Напишите функцию complex_operation, которая вызывает несколько вложенных функций и может вызвать исключение.
# # Если возникает исключение, перехватите его и извлеките "сырые" сведения о
# # трассировке стека с использованием traceback.extract_tb().
# # Выведите информацию о каждом фрейме стека (файл, строка, имя функции, текст строки).
#
# # Напишите тут ваш код
# import traceback
# import sys
#
# def function_c():
#     return 1 / 0  # Это вызовет ZeroDivisionError
#
# def function_b():
#     function_c()
#
# def complex_operation():
#     try:
#         function_b()
#     except ZeroDivisionError:
#         tb = sys.exc_info()[2]
#         for frame in traceback.extract_tb(tb):
#             print(f"Файл: {frame.filename}")
#             print(f"Линия: {frame.lineno}")
#             print(f"Имя функции: {frame.name}")
#             print(f"Текст: {frame.line}")
#             print("-" * 40)
#
# complex_operation()

import traceback

def complex_operation():
    def inner_function_1():
        def inner_function_2():
            def inner_function_3():
                # Здесь генерируем исключение
                raise ValueError("An error occurred")
            inner_function_3()
        inner_function_2()
    try:
        inner_function_1()
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        for frame in tb:
            print(f"File: {frame.filename}, Line: {frame.lineno}, Function: {frame.name}, Code: {frame.line}")

# Пример вызова функции
complex_operation()