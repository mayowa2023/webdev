lst = {"cashew", "guava", "mango", "Banana", "kiwi", "bicycle"}

print("Lenght of list:", len(lst))
#print("first Element:", lst[0])
print("last element:", lst[-1])

print("List before appending:", lst)
lst.append("Papaya")
print("updated list:", lst)

lst.remove("Guava")
print("updated list", lst)

lst.sort()
print("sorted list", lst)

lst.pop(1)
print("updated list", lst)

lst.reverse()
print("reversed list", lst)

print("Multiplication on list:", lst*2)
print("*", * 50)

lst1 = lst[:2]
print("sliced list:", lst1)

lst.clear()
print("/n updated list:", lst)