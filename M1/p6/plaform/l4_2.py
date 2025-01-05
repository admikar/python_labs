# nm = set()
# nl = []
# for i in range(5):
#     globals()["n"+str(i)] = {int(input("Enter number: "))}
#
# for i in range(5):
#     nm.update(globals()["n"+str(i)])
#
# print(nm)
#

initial_set = set()

for _ in range(5):
    number = int(input("Введите число: "))
    number_set = {number}
    initial_set.update(number_set)

print(initial_set)
