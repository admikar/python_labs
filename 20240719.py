lst = [1,2,3,4,5,6,7,8,8,8,9,9,9,9,9,9]

#new_lwt = set(lst)
#for el in lst:
#    print(lst.count(el))

tmp = []
for i in lst:
    if i not in tmp:
        tmp.append(i)

print(len(tmp), tmp)

lst[:] = sorted(set(lst))
print(len(lst), lst)

m_list_new = []

m_list_new = [x for x in m_list if x not in m_list_new]

