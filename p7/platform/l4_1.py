# student = {"name": "Alice", "age": 25}
#
# student["university"]="Oxford"
# print(student)
#
# if "city" not in student:
#     student["city"] = "London"
# print(student)
#
# student.update(country="UK")
# print(student)
# student.update(accomodation="yes")
# print(student)

# Создание словаря с информацией о студенте
student = {
    "name": "Иван",
    "age": 20
}

# Добавление нового элемента "университет"
student["университет"] = "МГУ"
print("После добавления 'университет':", student)

# Добавление элемента "город" только в том случае, если его еще нет в словаре
if "город" not in student:
    student["город"] = "Москва"
print("После возможного добавления 'город':", student)

# Добавление нескольких новых элементов с использованием метода update()
student.update({"факультет": "Физический", "курс": 3})
print("После добавления новых элементов с использованием update():", student)

