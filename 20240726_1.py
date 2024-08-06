# tuple1 = tuple([1,2,3])
#
# print(tuple1[1:2:22])
# ---

m_tuple = (1, 2, 3, 4)

a, b, *c = m_tuple

print(a, b, c)
print(a)
print(b)
print(c)

print(type(c))
