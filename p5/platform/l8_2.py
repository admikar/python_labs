
from random import randrange

o_list = [randrange(1, 20) for _ in range(10)]
n_list = list(o_list)
for _ in range(len(o_list) - 1, -1, -1):
    if o_list[_] % 2 == 0:
        del o_list[_]

print(o_list)
print(n_list)

