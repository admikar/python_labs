from random import randrange

o_list = [randrange(1, 100) for _ in range(10)]

n_list = list(o_list)

n_list.sort()

print(o_list)
print(n_list)