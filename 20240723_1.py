class1 = []
class2 = []
for _ in range(160, 177, 2):
    class1.append(_)

for _ in range(162, 181, 3):
    class2.append(_)
#class2 = [i for i in range(162, 180 + 1, 3)]

class1.extend(class2)

#class1 += class2

#class1 = sorted(class1)
class1.sort()

print(class1)


