# # Супермашины.
#
# # Создайте базовый класс Vehicle, который будет иметь атрибуты brand и model.
# # Затем создайте дочерний класс Car, который будет наследовать от Vehicle и добавлять атрибут fuel_type.
# # Используйте метод super() для вызова конструктора базового класса.
#
# # Напишите тут ваш код
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
# class Car(Vehicle):
#     def __init__(self, brand, model, fuel_type):
#         super().__init__(brand, model)
#         self.fuel_type = fuel_type
#

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

# Пример использования
car = Car("Toyota", "Corolla", "Petrol")
print(f"Brand: {car.brand}, Model: {car.model}, Fuel Type: {car.fuel_type}")
