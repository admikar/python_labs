# # Фигуры.
#
# # Создайте базовый класс Shape, который будет иметь метод area для вычисления площади.
# # Затем создайте два дочерних класса Rectangle и Circle, которые будут наследовать от Shape
# # и переопределять метод area для вычисления площади прямоугольника и круга соответственно.
#
#
#
# import math
#
# class Shape:
#     def area(self):
#         pass
#
# # Напишите тут ваш код
# class Rectangle(Shape):
#     def __init__(self, long, high):
#         self.long = long
#         self.high = high
#     def area(self):
#         return self.long * self.high
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * (self.radius**2)
#
#
# # Пример использования
# rect = Rectangle(3, 4)
# print(f"Area of rectangle: {rect.area()}")
#
# circle = Circle(5)
# print(f"Area of circle: {circle.area()}")
#

import math


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Пример использования
rect = Rectangle(3, 4)
print(f"Area of rectangle: {rect.area()}")

circle = Circle(5)
print(f"Area of circle: {circle.area()}")