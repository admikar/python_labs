# Создаем классы.

# Создайте класс Library с атрибутом books, который представляет собой список книг.
# Добавьте методы add_book(book) для добавления книги в библиотеку
# и display_books() для вывода списка всех книг.
# Создайте объект класса Library, добавьте несколько книг и выведите список книг, используя методы объекта.

# Напишите тут ваш код

# class Library:
#     books = []
#
#     def add_book(self, name):
#         self.books.append(name)
#
#     def display_books(self):
#         print(self.books)
#
#
# my_books = Library()
# my_books.add_book("New zeland")
# my_books.add_book("Cyprus")
#
# my_books.display_books()

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)


# Создание объекта класса Library
library = Library()

# Добавление нескольких книг
library.add_book("War and Peace")
library.add_book("1984")
library.add_book("The Great Gatsby")

# Вывод списка всех книг
library.display_books()