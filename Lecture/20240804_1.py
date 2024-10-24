# spisok = list()
# for i in range(-100, 101):
#     spisok.append(i ** 2)
#
# print(*spisok)
# print(spisok)
# spisok = []
# while True:
#     chislo = input("Введите число: ")
#     if chislo == "стоп":
#         break
#     else:
#         spisok.append(chislo)
#
# print(*spisok)
import random

# my_list = [10, 20, 30, 40, 50]
#
# print(len(my_list))
#
# print(my_list[0])
# print(my_list[-1])


# spisok = []
# for _ in range(1, 6):
#     spisok.append(input("Добавте элемент: "))
#
# print(*spisok)
#
# ind = int(input(f"write index from 0 till {len(spisok)-1} :"))
# print(spisok[ind])
import random


# import random
# random_list = [random.randint(0, 100) for _ in range(10)]
#
#
# print(random_list[2:7])
#
# print(random_list[-3:])
#
# print(*random_list)
#
# import random
# random_list = [random.randint(0, 100) for _ in range(10)]
# print(*random_list)
#
# stroka = int(input("Need string :"))
#
# print(stroka in random_list)

# import random
#
# random_list = [random.randint(0, 100) for _ in range(10)]
#
# for _ in range(3, 6):
#     number = input(f"Enter {_} element for exchamge :")
#     random_list[_] = number
#
# print(*random_list)
#
# numbers = [10, 20, 30, 40, 50]
#
# print(numbers.pop(7))

#
# import random
#
# random_list = [random.randint(0, 100) for _ in range(10)]
#
# for item, value in enumerate(random_list):
#     if value % 2 == 0:
#         random_list[item] = "четное"
#
# print(random_list)

# # Напишите тут ваш код
# lists = [ x ** 2 for x in range(1, 11)]
#
# print(lists)
#
# from random import randrange
#
# n = 10
# alist = [randrange(1, 10) for i in range(n)]

from random import randrange

alist = [randrange(1, 100) for i in range(20)]

slist = [x for x in alist if x % 2 == 0]

print(alist)
print(slist)