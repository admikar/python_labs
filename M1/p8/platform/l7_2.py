# # Платформа.
#
# # Напишите программу, которая получает и выводит информацию о текущей операционной системе
# # и платформе с помощью библиотеки platform. Программа должна:
# # Получить и вывести имя операционной системы.
# # Получить и вывести имя компьютера в сети (hostname).
# # Получить и вывести версию операционной системы.
# # Получить и вывести архитектуру процессора.
# # Получить и вывести версию Python.
#
# # Напишите тут ваш код
# import platform
#
# print("Operating System:", platform.system())
# print("Node Name:", platform.node())
# print("OS Version:", platform.version())
# print("Architecture:", platform.architecture())
# print("Python Version:", platform.python_version())
import platform
import socket

print("Имя операционной системы:", platform.system())
print("Имя компьютера в сети (hostname):", socket.gethostname())
print("Версия операционной системы:", platform.version())
print("Архитектура процессора:", platform.architecture()[0])
print("Версия Python:", platform.python_version())
