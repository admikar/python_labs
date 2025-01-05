n_list = []

for _ in range(5):
    n_list.append(input("Enter string:"))

n_list.sort(key=len)

print(n_list)