# # Работа с директориями.
#
# # Напишите программу, которая создает директорию, переходит в нее, создает файл внутри этой директории,
# # записывает в файл текст, а затем читает и выводит его содержимое.
# # Программа должна:
# # Создать директорию test_directory.
# # Перейти в директорию test_directory.
# # Создать файл test_file.txt и записать в него строку "Hello, World!".
# # Прочитать содержимое файла test_file.txt и вывести его на экран.
# # Удалить файл и директорию.
#
# # Напишите тут ваш код
# import os
# from time import sleep
#
# os.mkdir('test_directory')
#
# os.chdir('./test_directory')
#
# with open("test_file.txt", "w") as file:
#     file.write("Hello, World!\n")
#
# with open("test_file.txt", "r") as file:  # "r" означает чтение (read)
#     content = file.read()
#     print("Содержимое файла:")
#     print(content)
#
# os.remove("test_file.txt")
# os.chdir('..')
# os.rmdir('./test_directory')

import os

# Создаем директорию
os.makedirs('test_directory', exist_ok=True)

# Переходим в директорию
os.chdir('test_directory')

# Создаем файл и записываем в него строку
with open('test_file.txt', 'w') as file:
    file.write('Hello, World!')

# Читаем содержимое файла
with open('test_file.txt', 'r') as file:
    content = file.read()
    print(content)

# Удаляем файл
os.remove('test_file.txt')

# Переходим в родительскую директорию
os.chdir('..')

# Удаляем директорию
os.rmdir('test_directory')