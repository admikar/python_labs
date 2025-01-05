# # Защищайтесь.
#
# # Создайте класс Car, который будет иметь публичный атрибут brand и защищенный атрибут _model_.
# # Добавьте методы для получения и установки значения защищенного атрибута _model.
# # Создайте объект класса Car, установите значения атрибутов и выведите их на экран.
#
# # Напишите тут ваш код
#
# class Car:
#
#     def __init__(self):
#         self.brand = ""
#         self._model = ""
#
#     def get_model(self):
#         return self._model
#
#     def set_model(self, model):
#         self._model = model
#
# my_car = Car()
# my_car.brand = "Opel"
# my_car.set_model("Corsa")
#
# print(my_car.brand)
# print(my_car.get_model())

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model_ = model

    def get_model(self):
        return self._model_

    def set_model(self, model):
        self._model_ = model

# Создание объекта класса Car
car = Car("Toyota", "Camry")

# Установим новые значения для атрибутов
car.brand = "Honda"
car.set_model("Civic")

# Выводим значения атрибутов на экран
print(f"Brand: {car.brand}")
print(f"Model: {car.get_model()}")