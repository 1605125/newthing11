l1=[1,2,3,4]
d1={'l1':l1,'d2':{'a':1,'b':2},'t':(1,2,3,4)}
print(d1)
print((d1['d2']['a']))
#nested data structure
l2=[1,2,3,4]
d2={'a':1,'b':2}
t1=(l2,d2,1000)
t1[0].append(5)
t1[1].update({'c':3})
print(t1)
t1[0]='xyz'
t1[0][0]=100
print(t1)
