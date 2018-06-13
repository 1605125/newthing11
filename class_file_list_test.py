# take lst = [ 1, 2,3 ,4 5] and read it then convert it into squares and write and read its content in another file
from json import dumps, loads
lst = [1, 2, 3, 4, 5]
file = open("lstng", 'w')
file.write(dumps(lst))
file.close()


file = open("lstng")
data = file.read()
data = loads(data)
print("The original content of file is {}".format(data))
lst2 = []
for i in data:
    lst2.append(i*i)
with open('square', 'w') as f:
    f.writelines(dumps(lst2))
file = open("square")
data = file.read()
print("The square content of file is {}".format(data))




