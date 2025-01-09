# # Животный мир.
#
# # Создайте базовый класс Animal с методом make_sound, который будет возвращать строку "Ууууууу!".
# # Затем создайте дочерние классы Dog и Cat, которые будут переопределять метод make_sound
# # и использовать super() для вызова метода родительского класса.
#
# # Напишите тут ваш код
# class Animal:
#     def make_sound(self):
#         return f"Ууууууу!"
#
# class Dog(Animal):
#     def make_sound(self):
#         parent_sound = super().make_sound()  # Вызываем метод родительского класса
#         return f"{parent_sound} Гав-гав!"
#
# class Cat(Animal):
#     def make_sound(self):
#         parent_sound = super().make_sound()  # Вызываем метод родительского класса
#         return f"{parent_sound} Мяу-мяу!"
#
#
# # Примеры использования:
# dog = Dog()
# cat = Cat()
#
# print(dog.make_sound())  # Ууууууу! Гав-гав!
# print(cat.make_sound())  # Ууууууу! Мяу-мяу!

class Animal:
    def make_sound(self):
        return "Ууууууу!"

class Dog(Animal):
    def make_sound(self):
        return super().make_sound() + " Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return super().make_sound() + " Мяу-мяу!"

# Примеры использования:
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Ууууууу! Гав-гав!
print(cat.make_sound())  # Ууууууу! Мяу-мяу!