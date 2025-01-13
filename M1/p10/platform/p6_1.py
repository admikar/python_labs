# # Пользовательское исключение
#
# # Создайте пользовательское исключение InvalidAgeError, которое будет вызываться в функции check_age,
# # если возраст меньше 0 или больше 150. Обработайте это исключение в блоке try-except.
#
# # Напишите тут ваш код
# class InvalidAgeError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)
#
#
# def check_age(age):
#     if age < 0:
#         raise InvalidAgeError("Less 0")
#     elif age > 150:
#         raise InvalidAgeError("More 150")
#
#
# try:
#     age = int(input("Enter your age: "))
#     check_age(age)
#     print("Age is valid.")
# except InvalidAgeError as e:
#     print(e)
# except ValueError:
#     print("Please enter a valid integer for age.")

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(f"Invalid age: {age}")

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer for age.")