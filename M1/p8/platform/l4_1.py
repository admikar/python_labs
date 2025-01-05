# # Декоратор.
#
# # Напишите программу, которая создает простой декоратор для логирования вызовов функции.
# # Программа должна:
# # Определить декоратор log_decorator, который выводит сообщение перед и после вызова функции.
# # Применить декоратор к функции greet(), которая выводит приветственное сообщение.
# # Вызвать функцию greet().
#
# # Напишите тут ваш код
# def log_decorator(func):
#     def wrapper():
#         print("Перед вызовом функции")
#         func()
#         print("После вызова функции")
#
#     return wrapper
#
# @log_decorator
# def greet():
#     print("Hello!")
#
# greet()

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Перед вызовом функции")
        result = func(*args, **kwargs)
        print("После вызова функции")
        return result
    return wrapper

@log_decorator
def greet():
    print("Привет!")

greet()

