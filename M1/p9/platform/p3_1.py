# # # Создаем объекты.
# #
# # # Создайте класс Car с атрибутами make, model и year.
# # # Добавьте метод display_info(), который выводит информацию о машине.
# # # Затем создайте объект этого класса и вызовите метод display_info().
# #
# # # Напишите тут ваш код
# # class Car:
# #     make = "No"
# #     model = "Opel"
# #     year = 2025
# #
# #     @classmethod
# #     def display_info(cls):
# #         print(f'{cls.make} and {cls.model} and {cls.year}')
# #
# # new_car = Car()
# #
# # new_car.display_info()
#
# class Car:
#     make = "No"
#     model = "Opel"
#     year = 2025
#
#     def display_info(self):
#         print(f'{self.make} and {self.model} and {self.year}')
#
#
# new_car = Car()
#
# new_car.display_info()

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Создание объекта класса Car
my_car = Car("Toyota", "Camry", 2020)

# Вызов метода display_info()
my_car.display_info()