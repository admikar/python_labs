# # Импорт элементов из модуля
#
# # Создайте модуль geometry.py, который содержит функции circle_area(radius) и rectangle_area(length, width).
# # Затем импортируйте только функцию circle_area и используйте её в другом файле.
#
# # Напишите тут ваш код
# from geometry import circle_area
#
# print(circle_area(5))

from geometry import circle_area

radius = 5
area = circle_area(radius)
print(f"Площадь круга с радиусом {radius} равна {area}")

