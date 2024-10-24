# my_tuple = ('a', 'b', 'c', 'd')
# print(len(my_tuple))

# nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# summa = 0
# for inner_tuple in nested_tuple:
#     for number in inner_tuple:
#         summa += number
# print(summa)

nested_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

total_sum = 0
for inner_tuple in nested_tuples:
    for num in inner_tuple:
        total_sum += num

print(total_sum)
