s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 4, 4}
temp = s1.intersection(s2)
print(temp)
print("-----------------------------")
#intersection update
s1.intersection_update(s2)
print(s1)
print(s2)
print("------------------------------------")
s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 4, 4}
temp = s1.union(s2)
print(temp)
temp = s2.issubset(s1)
print(temp)