# # # # # import sys
# # # # #
# # # # # for path in sys.path:
# # # # #     print(path)
# # # # obj = []
# # # # iterator = iter(obj)
# # # # print(dir(obj))
# # # # print(dir(iterator))
# # #
# # # module_name = "math"
# # # module = __import__(module_name)
# # # print(module.sqrt(16))
# # import math
# #
# # # Получаем атрибут sqrt из модуля math
# # sqrt_function = getattr(math, 'sqrt')
# #
# # print(sqrt_function(25))  # Вывод: 5.0
# #
# # # Пытаемся получить несуществующий атрибут, возвращаем значение по умолчанию
# # non_existent_attr = getattr(math, 'non_existent', 'default_value')
# #
# # print(non_existent_attr)  # Вывод: default_value
#
# ##input
# #math
# #sqrt
#
# module_name = input("Enter name of python module")
# func_name = input("Enter name of function inside module")
#
# module = __import__(module_name)
#
# my_function = getattr(module, func_name)
#
# print(my_function(25))

