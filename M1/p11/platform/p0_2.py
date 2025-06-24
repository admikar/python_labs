# # Динамический импорт модуля
#
# # Напишите программу, которая запрашивает у пользователя название модуля для импорта
# # и имя функции для вызова из этого модуля.
# # Программа должна динамически импортировать модуль и вызвать указанную функцию с любым аргументом.
# # Для получения дочернего элемента у модуля используйте функцию getattr
#
# # Напишите тут ваш код
# module_name = input("Enter name of python module")
# func_name = input("Enter name of function inside module")
#
# module = __import__(module_name)
#
# my_function = getattr(module, func_name)
#
# my_function(25)
#
module_name = input("Введите название модуля: ")
function_name = input("Введите имя функции: ")

module = __import__(module_name)
function = getattr(module, function_name)

function(1)