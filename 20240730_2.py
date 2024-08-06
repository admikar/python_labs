# Напишите программу, которая находит все различные цифры в символьной строке. Для решения используйте множество (цифры будут различные, и поиск во множестве намного быстрее, чем в списке).
#  
# Подсказка: можно использовать вот такое сравнение '0'<=x<='9'
#  
# Пример:
# Введите строку: ab1n32kz2
# Различные цифры строки: 123


data = set(input("Write string: "))
result = []
for i in data:
    if i.isdigit():
        result.append(i)

print(*result, sep='')




# my_set = set(str(input("Введите строку: ")))
# my_set_1 = set()
# for element in my_set:
#     if '0' <= element <= '9':
#         my_set_1.add(element)
# print("Различные цифры строки: ", my_set_1)


# print(set([x for x in string if x.isdigit()]))


# string = input("Введите строку: ")
# my_list = []
# [my_list.append(char) for char in string if char.isdigit() == True]
# print(set(my_list))


# text = input()
# me_set = set()
# for char in text:
#     if char.isdigit():
#         me_set.add(int(char))
# print(*me_set)



st = input() #isdigit
m_set = set()
for i in st:
    if i.isdigit():
        m_set.add(i)

print(*m_set, sep="")

st = input() #isdigit

print(*set(filter(lambda x: x.isdigit(), st)), sep="")