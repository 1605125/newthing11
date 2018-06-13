# example 1
l1 = range(1, 6)
data = map(lambda x: x * x, l1)
print(list(data))
# example 2
print("----------example 2-------------")


def sqr(item):
    return item * item


l2 = range(1, 6)
data1 = map(sqr, l2)
print(list(data1))
print("-------------example 3-----------")


def sqr(item1, item2):
    return item1 * item2


m1 = [1, 2, 3, 4, 5]
m2 = [10, 20, 30, 40, 50, 60]
d = map(lambda x, y: x * y, m1, m2)
# d = map(sqr, m1, m2)
print(list(d))

print("-----------------------filter---------------")
n1 = [1, 2, 3, 4, 5]
di = map(lambda x: x * x if x % 2 == 0 else x, n1)
print(list(di))

print("\n")
dm = filter(lambda x: x * x if x % 2 == 0 else x, n1)
print(list(dm))  # we cannot modify using filter function

print("\n\nmap and filter another example")
c1 = [1, 2, 3, 4, 5]
data = map(lambda x: x % 2 == 0, c1)
print(list(data))

data = filter(lambda x: x % 2 == 0, c1)
print(list(data))
