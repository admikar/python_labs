# # Три проверки.
#
# # Напишите программу, которая создает словарь с информацией о книге (например, название, автор, год издания).
# # Программа должна:
# # Проверить наличие ключа "author" с использованием оператора in.
# # Проверить наличие ключа "publisher" с использованием метода get().
# # Проверить наличие ключа "title" с использованием метода keys().
#
# # Напишите тут ваш код
# book_info = {
#     "title": "Преступление и наказание",
#     "author": "Федор Достоевский",
#     "year": 1866
# }
# print("author" in book_info)
#
# value = book_info.get("publisher")
#
# if value is not None:
#     print("publisher keys inside")
# else:
#     print("publisher keys not inside")
#
# if "title" in book_info.keys():
#     print("title keys inside")
# Создаем словарь с информацией о книге
book_info = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": 1960
}

# Проверка наличия ключа "author" с использованием оператора in
if "author" in book_info:
    print("Ключ 'author' найден")

# Проверка наличия ключа "publisher" с использованием метода get()
if book_info.get("publisher") is not None:
    print("Ключ 'publisher' найден")
else:
    print("Ключ 'publisher' не найден")

# Проверка наличия ключа "title" с использованием метода keys()
if "title" in book_info.keys():
    print("Ключ 'title' найден")