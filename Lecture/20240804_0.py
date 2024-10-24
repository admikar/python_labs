# def find_max(a, b):
#     if a >= b:
#         return a
#     else:
#         return b
#
#
# first_number = int(input("Insert first number: "))
# second_number = int(input("Insert second number: "))
#
# print(find_max(first_number, second_number))

# def factorial(n):
#     result = 1
#
#     if n == 0:
#         return 1
#     else:
#         for i in range(1, n+1):
#             result *= i
#         return result
# print(factorial(3))

# def calculate_total_cost(price, tax=0.2):
#     result = price * tax + price
#     print(result)
#
# calculate_total_cost(100)
# calculate_total_cost(100, 0.50)
#
# def create_cat_profile(name, age, breed="Неизвестно"):
#     print(f"Имя: {name} Возраст: {age}, Порода: {breed}")
#
# create_cat_profile("Barsik", 1)
# create_cat_profile("Tusik", 30, "pes")


# counter = 0
#
#
# def increment_counter():
#     global counter
#     counter += 1
#
#
# increment_counter()
# increment_counter()
# increment_counter()
#
# print(counter)
#
# def sum_numbers(*args: int) -> int:
#     summ = 0
#     for item in args:
#         summ += item
#     return summ
#
# print(sum_numbers(1,2,3))
# print(sum_numbers(1,2,3,4,5))
# print(sum_numbers(8,9))

# def create_cat_profile(name: str, age: int, **kwargs: str) -> None:
#     desctibe = f"Кота зовут {name}, ему {str(age)} лет, у него "
#     print(f'{desctibe.join(f"{key} {value}," for key, value in kwargs.items())}')
#
# create_cat_profile("Мурзик", 3, порода="Сиамский", цвет="Черный")
# create_cat_profile("Барсик", 5, страна="Китай", хобби="Ловить мышей")
def outer():
    

    def inner():
        nonlocal count
        count += 1
        return count

    return inner

counter = outer()
print(counter())