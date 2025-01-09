# # Базовые классы.
#
# # Создайте два базовых класса Base1 и Base2, каждый из которых имеет метод describe().
# # Создайте производный класс Combined, который наследует от обоих базовых классов.
# # Реализуйте метод describe() в каждом базовом классе. Вызовите метод describe() у объекта класса Combined.
#
# # Напишите тут ваш код
#
class Base1:
    def describe(self):
        print(f"Class Base1")
        super().describe()


class Base2:
    def describe(self):
        print(f"Class Base2")

class Combined(Base1, Base2):
    def describe(self):
        print(f"Class Combined")
        super().describe()


check = Combined()

check.describe()







# class Base1:
#     def method(self):
#         print("Method from Base1")
#         super().method()
#
# class Base2:
#     def method(self):
#         print("Method from Base2")
#
# class Derived(Base1, Base2):
#     def method(self):
#         print("Method from Derived")
#         super().method()
#
#
# obj = Derived()
# obj.method()



# class A:
#     def method(self):
#         print("Method from A")
#
# class B(A):
#     def method(self):
#         print("Method from B")
#         super().method()
#
# class C(A):
#     def method(self):
#         print("Method from C")
#         super().method()
#
# class D(B, C):
#     def method(self):
#         print("Method from D")
#         super().method()
#
#
#
# obj = D()
# obj.method()