#
# def set_detector(*argv):
#     mn_count = 0
#     for _ in argv:
#         if type(_) is set:
#             mn_count += 1
#     return bool(mn_count)
#
# print(set_detector("STrings", {1,2,3,4}, [1,2,3,4,5]))
# print(set_detector("STrings", (1,2,3,4), [1,2,3,4,5]))
#

def set_detector(*args):
    for arg in args:
        if type(arg) == set:
            return True
    return False

# Вызовы функции с разными вариантами параметров
print(set_detector(1, [2, 3], (4, 5), {6, 7}))  # Множество присутствует
print(set_detector(1, [2, 3], (4, 5)))  # Множество отсутствует
print(set_detector("hello", 10, {1, 2, 3}))  # Множество присутствует
print(set_detector("world", 42, 3.14))  # Множество отсутствует