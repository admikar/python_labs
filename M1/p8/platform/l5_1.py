# # Множество декораторов.
#
# # Напишите программу, которая использует несколько декораторов для одной функции.
# # Программа должна:
# # Определить два декоратора decorator1 и decorator2, которые логируют свои вызовы.
# # Применить оба декоратора к функции say_hello.
# # Вызвать функцию say_hello.
#
# # Напишите тут ваш код
# def decorator1(func):
#     def wrapper():
#         print("Декоратор 1")
#         func()
#
#     return wrapper
#
# def decorator2(func):
#     def wrapper():
#         print("Декоратор 2")
#         func()
#
#     return wrapper
#
# @decorator1
# @decorator2
# def say_hello():
#     print("Hello!")
#
# say_hello()
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Before function call")
        result = func(*args, **kwargs)
        print("Decorator 1: After function call")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2: Before function call")
        result = func(*args, **kwargs)
        print("Decorator 2: After function call")
        return result
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello, world!")

say_hello()

