# # # #open file
# # # file = open('file.txt')
# # # #read all file
# # # print(file.read())
# # # #read all lines in list
# # # print(file.readlines())
# # # #read on line
# # # print(file.readline())
# # # file.close()
# #
# #
# #
# # #open file
# # file = open('file1.txt', 'w', encoding='utf-8')
# # file.write('Hello\n')
# # file.write('world')
# # file.close()
# #
# # # w - rewrite
# # # a - append
# # # r - read
# # # r+ - read and write
# # # w+ - or create new
# # # a+ - add or create new
# #
# # # 5 - count symbols and stop cursor
# # print(file.tell())
# #
# # print(file.read(5))
# # # tell me where in file we in bytes
# # print(file.tell())
# # ## utf-8  - 1 symbol use 2 bytes
# #
# # #move on n's bytes
# # file.seek(8)
# #
# # print(file.read(5))
# #
# # #or
# # file = open('file.txt')
# # for line in file:
# #     print(line.strip())
#
# #with close file
# with open('file.txt') as file:
#     context = file.readlines()
# from sys import getsizeof
# #getsizeof()
#

import shutil
import os
import sys

print(os.name)
#print(os.path.basename())
print(os.cpu_count())
