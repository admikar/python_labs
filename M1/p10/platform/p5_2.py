# # Переупаковка исключения
#
# # Напишите функцию validate_input, которая принимает строку и проверяет,
# # что она не пустая и что ее длина не превышает 10 символов.
# # Если строка пустая, запустите ValueError с сообщением "Input cannot be empty".
# # Если строка слишком длинная, запустите ValueError с сообщением "Input is too long".
# # Затем перехватите это исключение и переупакуйте его в пользовательское исключение InputValidationError, сохранив исходное исключение как причину.
#
# # Напишите тут ваш код
# # Пользовательское исключение
# class InputValidationError(Exception):
#     def __init__(self, message, original_exception=None):
#         self.message = message
#         self.original_exception = original_exception  # Сохраняем оригинальное исключение
#         super().__init__(self.message)
#
#     def __str__(self):
#         return f'{self.message}'
#
# # Функция валидации
# def validate_input(f_string):
#     try:
#         # Проверяем строку на длину
#         if len(f_string) == 0:
#             raise ValueError("Input cannot be empty")
#         if len(f_string) > 10:
#             raise ValueError("Input is too long")
#     except ValueError as e:
#         # Переупаковываем ValueError в InputValidationError
#         raise InputValidationError("Validation failed", original_exception=e)
# # Пример использования:
# try:
#     validate_input("")
# except InputValidationError as e:
#     print(f"Caught custom exception: {e}")
#     print(f"Original exception: {e.original_exception}")
#
#


class InputValidationError(Exception):
    def __init__(self, message, original_exception):
        super().__init__(message)
        self.original_exception = original_exception

def validate_input(input_str):
    try:
        if not input_str:
            raise ValueError("Input cannot be empty")
        if len(input_str) > 10:
            raise ValueError("Input is too long")
    except ValueError as e:
        raise InputValidationError("Validation error occurred", e)

# Пример использования:
try:
    validate_input("")
except InputValidationError as e:
    print(f"Caught custom exception: {e}")
    print(f"Original exception: {e.original_exception}")