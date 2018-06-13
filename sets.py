# sets have unique value
s1={1,2,2,3,3,3,4,4,4,4,5,5,5,5,5}
l1=[1,2,3,4,5,2,3,4,5,6,4,3,2,1]
l1=set(l1)#by this extra list is removed
l1=list(l1) #type converion used two times
print(l1)
print(s1)
#adding single items to set
s1.add('abc')
s1.add(100)
s1.add(1)
#
print("after addding {}".format(s1))
s1.update([1,2,3,4,5,'cde',6,7])
print("after update {}".format(s1))
s1.pop()
# s1.remove(9)
s1.discard(7)
print(s1)