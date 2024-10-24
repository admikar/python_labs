# # def outer():
# #     count = 0
# #
# #     def inner():
# #         nonlocal count
# #         count += 1
# #         return count
# #
# #     return inner
# #
# # counter = outer()
# # print(counter())
# # ---
# col_list = list([1, 2, 3])
# tuples = tuple([1, 2, 3])
# my_set = set({1, 2, 3})
# my_dict = dict({'a': 1, 'b': 2})
# my_frozenset = frozenset([1, 2, 3])
#
#
# print(col_list)
# print(tuples)
# print(my_set)
# print(my_dict)
# print(my_frozenset)
# # ---
# a=4
# b=2
# result = a / b
# print(result)
# print(type(result))
#
# # ---

import random

summa = 0
for i in range(1, 11):
    chislo = random.randint(1, 100)
    summa += chislo

print(summa / 10)
