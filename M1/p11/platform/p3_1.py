# # import requests
# #
# # print(requests.get('https://jsonplaceholder.typicode.com').text)
# #
# # print(requests.get('https://jsonplaceholder.typicode.com').json)
# #
# #
# # Добавьте код для вывода содержимого ответа запроса на экран. Используйте метод .text или .json() для вывода содержимого.
# #
# # Используйте метод .text или .content для вывода результата запроса, например, print(requests.get('https://jsonplaceholder.typicode.com').text).
# # Использование пакета requests.
#
# # Используйте пакет requests для выполнения GET-запроса к API.
# # Выполните следующие шаги:
# # Установите пакет requests с помощью pip.
# # Используйте пакет requests для выполнения GET-запроса к API, например, к https://jsonplaceholder.typicode.com.
# # Выведите на экран результат запроса.
#
# # Напишите тут ваш код
# #pip install requests
# import requests
#
# print(requests.get('https://jsonplaceholder.typicode.com').text)
#
#
#

import requests

# Выполнение GET-запроса к API
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Вывод результата запроса
print(response.json())

