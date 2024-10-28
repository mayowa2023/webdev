my_set = (1,2,2,3,4,4,4)
print("set:", my_set)

my_set.add(5)
print("Updated set:",my_set)

set1 = my_set
set2 = {2,4,4,6}

print("/nset1:", set1)
print("/nset2:", set2)
print("Diffrence")
print(set1.diffrence(set2))
print("Symentric diffrence")
print(set1.symentric_diffrence(set2))