# worker = [("Ivan", "Engineer"), ("Ian", "Enginer"), ("Kostya", "balabol")]
#
# worker_dict = {key: value for key, value in worker}
#
# print(worker_dict)
#
# # # Список списков с парами ключ-значение
# # nested_pairs = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
# #
# # # Генерация словаря из вложенного списка
# # nested_dict = {key: value for sublist in nested_pairs for key, value in sublist}
# # print(nested_dict)  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Список кортежей с информацией о сотрудниках
employees = [("Иван", "Инженер"), ("Мария", "Менеджер"), ("Петр", "Аналитик")]

# Создание словаря с использованием dictionary comprehension
employee_dict = {name: position for name, position in employees}

# Вывод созданного словаря
print(employee_dict)