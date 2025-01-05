# # Холодные ключи
#
# # Напишите программу, которая создает несколько объектов типа frozenset и использует их в качестве ключей в словаре.
# # Программа должна:
# # Создать два frozenset из списков.
# # Создать словарь, где ключами являются frozenset, а значениями строки.
# # Вывести словарь.
#
# # Напишите тут ваш код
# fset1 = frozenset([1, 2, 3])
# fset2 = frozenset([3, 4, 5])
#
# d = {fset1: "first", fset2: "second"}
# print(d)
# Создаем два frozenset из списков
#from tatsu.util import to_list

frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([4, 5, 6])

# Создаем словарь, где ключами являются frozenset, а значениями строки
dictionary = {
    frozenset1: "Первый набор чисел",
    frozenset2: "Второй набор чисел"
}

# Выводим словарь
print(dictionary)

