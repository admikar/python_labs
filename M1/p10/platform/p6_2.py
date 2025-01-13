# # Иерархия пользовательских исключений
#
# # Создайте базовый класс исключений ApplicationError и два подкласса NegativeValueError и ValueTooLargeError.
# # Реализуйте функцию check_number, которая будет вызывать соответствующее исключение, если число отрицательное или слишком большое.
# # Обработайте исключения в блоке try-except.
#
# # Напишите тут ваш код
#
# class ApplicationError(Exception):
#     """Базовый класс для всех исключений приложения."""
#     pass
#
# class NegativeValueError(ApplicationError):
#     """Класс для пользовательского исключения при отрицательном значении."""
#     def __init__(self, value, message="Значение не должно быть меньше нуля"):
#         self.value = value
#         self.message = message
#         super().__init__(self.message)
#
#     def __str__(self):
#         return f'{self.message}: {self.value}'
#
# class ValueTooLargeError(ApplicationError):
#     """Класс для пользовательского исключения при слишком большом значении."""
#     def __init__(self, value, message="Значение слишком велико"):
#         self.value = value
#         self.message = message
#         super().__init__(self.message)
#
#     def __str__(self):
#         return f'{self.message}: {self.value}'
#
# def check_number(value):
#     if value < 0:
#         raise NegativeValueError(value)
#     elif value > 100:
#         raise ValueTooLargeError(value)
#
# try:
#     check_number(150)
# except NegativeValueError as e:
#     print(f"Произошло исключение: {e}")
# except ValueTooLargeError as e:
#     print(f"Произошло исключение: {e}")

class ApplicationError(Exception):
    pass

class NegativeValueError(ApplicationError):
    pass

class ValueTooLargeError(ApplicationError):
    pass

def check_number(number):
    if number < 0:
        raise NegativeValueError("The value is negative.")
    elif number > 100:
        raise ValueTooLargeError("The value is too large.")
    else:
        return "The value is acceptable."

try:
    num = int(input("Enter a number: "))
    result = check_number(num)
    print(result)
except NegativeValueError as e:
    print(f"Error: {e}")
except ValueTooLargeError as e:
    print(f"Error: {e}")
except ApplicationError as e:
    print(f"An application error occurred: {e}")