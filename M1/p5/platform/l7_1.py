from random import randrange

o_list = [randrange(1, 100) for _ in range(10)]

ns_list = sorted(o_list)
nr_list = sorted(o_list, reverse=True)

print(o_list)
print(ns_list)
print(nr_list)

