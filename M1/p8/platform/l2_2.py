# def make_filter(threshold):
#     def filter_func(value):
#         return value > threshold
#     return filter_func
#
# a1 = make_filter(10)
# a2 = make_filter(20)
#
# data = [5, 10, 15, 20, 25, 30]
#
# print(list(filter(a1, data)))
# print(list(filter(a2, data)))

def make_filter(threshold):
    def filter_func(value):
        return value > threshold
    return filter_func

# Создаем несколько фильтрующих функций с различными пороговыми значениями
filter_10 = make_filter(10)
filter_20 = make_filter(20)
filter_30 = make_filter(30)

# Список данных для фильтрации
data = [5, 15, 25, 35, 45]

# Фильтруем данные и выводим результаты
print(list(filter(filter_10, data)))  # Должен вывести [15, 25, 35, 45]
print(list(filter(filter_20, data)))  # Должен вывести [25, 35, 45]
print(list(filter(filter_30, data)))  # Должен вывести [35, 45]