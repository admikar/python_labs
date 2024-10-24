# # fruits = {"apple", "banana", "cherry"}
# #
# # while fruits:
# #     fruit = input("Enter name fruit: ")
# #     if fruit in fruits:
# #         fruits.discard(fruit)
# #         print(fruits)
# # Напишите тут ваш код
# fruits = {"apple", "banana", "cherry"}
#
# while fruits:
#     fruit = input("Enter name fruit: ")
#     fruits.discard(fruit)
#     print(fruits)

# Создаем множество с названиями фруктов
fruits = {"яблоко", "банан", "апельсин", "груша", "персик"}

# Запрашиваем у пользователя название фрукта для удаления
fruit_to_remove = input("Введите название фрукта для удаления: ")

# Удаляем фрукт из множества, если он есть
fruits.discard(fruit_to_remove)

# Выводим обновленное множество
print("Обновленное множество фруктов:", fruits)