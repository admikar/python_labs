# cats = {"Barsic", "Tuzic", "Puzic", "Smuzic", "Pupuzic"}
# counts = 0
# while cats:
#     cat = input("Enter name cat: ")
#     counts += 1
#     cats.discard(cat)
#
# print(counts)

popular_cat_names = {"Барсик", "Мурка", "Васька", "Снежок", "Мурзик"}

attempts = 0

while popular_cat_names:
    guess = input("Угадайте имя кота: ")
    attempts += 1
    if guess in popular_cat_names:
        popular_cat_names.remove(guess)
        print(f"Верно! Осталось угадать: {len(popular_cat_names)} имен.")
    else:
        print("Неверно. Попробуйте снова.")

print(f"Вы угадали всех котов за {attempts} попыток!")