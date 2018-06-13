l1 = [1, 2, 3, 4, 5]
temp = enumerate(l1)

print(dict(list(temp)))


for i, v in enumerate(l1):
     print(str(i) + '=>' +str(v))
