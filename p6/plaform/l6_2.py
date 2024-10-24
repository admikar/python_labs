# fruits = {"apple", "banana", "peach", "pear"}
#
# print(fruits)
#
# # index, fruit = input("Enter index of fruit and name of fruit: ").split()
# index = input("Enter index of fruit ")
# fruit = input("Enter name of fruit: ")
#
# new_est = set()
# for inx, elem in enumerate(fruits):
#     if inx == int(index):
#         new_est.add(fruit)
#     else:
#         new_est.add(elem)
#
# print(new_est)
#
#
fruits = {"яблоко", "банан", "апельсин", "груша"}

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

index = int(input("Введите номер фрукта для замены: ")) - 1
new_fruit = input("Введите новое название фрукта: ")

fruits_list = list(fruits)
fruits_list[index] = new_fruit
fruits = set(fruits_list)

print("Обновленное множество фруктов:", fruits)