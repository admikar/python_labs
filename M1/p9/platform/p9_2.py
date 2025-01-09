# # Автопарк.
#
# # Напишите функцию check_subclass для проверки, является ли один класс подклассом другого.
# # Используйте функцию issubclass() для выполнения проверки.
# # Затем создайте классы Vehicle, Car, Bicycle, и проверьте, являются ли Car и Bicycle подклассами Vehicle.
#
# # Напишите тут ваш код
#
# class Vehicle:
#     pass
# class Car(Vehicle):
#     pass
# class Bicycle(Vehicle):
#     pass
#
# def check_subclass(f_class, s_class):
#     return issubclass(f_class, s_class)
#
# print(check_subclass(Vehicle, Car))
# print(check_subclass(Bicycle, Car))
# print(check_subclass(Car, Vehicle))
# print(check_subclass(Bicycle, Vehicle))
# print(check_subclass(Vehicle, Bicycle))
# print(check_subclass(Car, Bicycle))
# print(check_subclass(Bicycle, Bicycle))
#

def check_subclass(class1, class2):
    return issubclass(class1, class2)

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

# Проверка
print(check_subclass(Car, Vehicle))  # Должно вернуть True
print(check_subclass(Bicycle, Vehicle))  # Должно вернуть True
