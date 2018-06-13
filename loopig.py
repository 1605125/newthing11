# l1="efgfg"
# for i in l1:
#     print(i)
#     #print(l1)
# else:
#     print("empty list")
l2 = range(1, 11)
if len(l2) == 0:
    print("empty")
else:
    for i in l2:
        print(i)
#generate odd numbers
l1 = range(0,11,2)
l1=list(l1)
print(l1)
#generate even numbers
l1 = range(1,11,2)
l1 = list(l1)
print(l1)
d1 = {"a": 1, "b": 6}
for i in d1:
    print(i)
#for diaplasying both key and values
for k, v in d1.items():
    print(k + ':' + str(v))
# iterating sets
s1 = {1, 2, 3, 4, 5}
for i in s1:
    print(i)

