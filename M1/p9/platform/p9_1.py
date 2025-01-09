# # Домашние животные.
#
# # Напишите функцию check_type для проверки, является ли переданный объект экземпляром класса Animal или его подклассов.
# # Используйте функцию isinstance() для выполнения проверки.
# # Затем создайте классы Animal, Dog, Cat и проверьте несколько объектов.
#
# # Напишите тут ваш код
#
# class Animal:
#     def __init__(self):
#         animal = "Animal"
#
#
# class Dog(Animal):
#     def __init__(self):
#         dog = "Dog"
#
#
# class Cat(Animal):
#     def __init__(self):
#         cat = "Cat"
#
#
# def check_type(check_class, need_class):
#     return isinstance(check_class, need_class)
#
# animal = Animal()
# dog = Dog()
# cat = Cat()
#
# MyClass = type('MyClass', (), {'say_hello': lambda self: print("Hello!")})
# instance = MyClass()
#
# print(check_type(animal, Animal))
# print(check_type(dog, Animal))
# print(check_type(cat, Animal))
# print(check_type(instance, Animal))
#
#

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

def check_type(obj):
    return isinstance(obj, Animal)

# Примеры использования:
dog = Dog()
cat = Cat()
not_animal = "Not an animal"

print(check_type(dog))  # True
print(check_type(cat))  # True
print(check_type(not_animal))  # False