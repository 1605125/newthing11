l1=[1,2,3]
l2=l1
l1.append(4)#reassignment not used
print(l1)
print(l2)
#l1 and l2 after coping points to same memory location
l1=l1*3#reassignment operator used
print(l1)
print(l2)