# В честь своего дня рождения Артём решил закатить вечеринку у себя на даче. Он не стал рассылать приглашения, а просто сообщил всем: «Если хотите — приходите и своих друзей тоже зовите». Люди приходили и уходили во время вечеринки, ночевать остались не все. К тому же и сама дача не резиновая — на ней помещается всего шесть человек.
# Дан изначальный список гостей — имена тех, кто пришёл к началу:
# guests = [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
# Напишите программу, которая спрашивает у пользователя, ушёл или пришёл гость и, исходя из ответа, добавляет в список или удаляет из него нужное имя. При этом гостей может быть не больше шести. Имена запрашиваются до тех пор, пока пользователь не введёт сообщение «Пора спать».
# Пример:
# # Сейчас на вечеринке 5 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
# # Гость пришёл или ушёл? пришёл
# # Имя гостя: Алекс
# # Привет, Алекс!
# # Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
# # Гость пришёл или ушёл? пришёл
# # Имя гостя: Гоша
# # Прости, Гоша, но мест нет.
# # Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
# # Гость пришёл или ушёл? ушёл
# # Имя гостя: Ваня
# # Пока, Ваня!
# # Сейчас на вечеринке 5 человек: [‘Петя’, ‘Саша’, ‘Лиза’, ‘Катя’,  ‘Алекс’]
# # Гость пришёл или ушёл? Пора спать
# # Вечеринка закончилась, все легли спать.
#
#
# # # count_guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
# # #
# # # enter = "Сейчас на вечеринке 5 человек"
# # #
# # # while (enter != "Пора спать"):
# # #     if len(count_guests) <= 6:
# # #         print(f"Сейчас на вечеринке {len(count_guests)} человек: {count_guests}")
# # #         enter = input("Гость пришёл или ушёл? ")
# # #         if enter == "пришёл":
# # #             new_
# # #             count_guests.append(enter)
# # #         elif enter == "ушёл":
# # #             count_guests.remove()
# # # --- lesha
# # guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
# #
# # while True:
# #     print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
# #     user_input = input("Гость пришёл или ушёл? ")
# #     if user_input == "пора спать":
# #         print("Вечеринка закончилась, все легли спать")
# #         break
# #     elif user_input == "пришёл":
# #         name = input("Имя гостя: ")
# #         if len(guests) < 6:
# #             print(f"Привет, {name}!")
# #             guests.append(name)
# #         else:
# #             print(f"Прости {name}, но мест нет")
# #             continue
# #     elif user_input == "ушёл":
# #         name = input("Имя гостя: ")
# #         if name in guests:
# #             guests.remove(name)
# #         else:
# #             print("Гость не найден")
# #             continue
# #     else:
# #         print("Неверный ввод")
# #         print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
#
#
