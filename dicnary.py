#dictionary does not support slicing
d1={'name':'Raju',
    'email':'raju@gmail.com',
    'city':'bangalore',
    'phone':7993231908
}
print(d1)
d1['name']='xyz'#updating exsisting one
print(d1)
d1.update({'address:':'btm'})
print(d1)
d1.update({'pincode':5600090,'age':23})
print(d1)
d1['area']='lake'#updation
print(d1)
d1.pop('name')#pop function
print(d1)
del d1['city']#del function
print(d1)
#get function is for getting values from the keys
print(d1.get('email'))
#key function
temp=d1.keys()
print(list(temp))
#value function it will pull out all the values
tem1=d1.values()
print(list(tem1))
#copy
d2=d1.copy()
d1.update({'200':'133'})
print(d1)
print(d2)
#item function
for k,v in d1.items():
    print(d1[k])
#without item function
for k in d1:
    print(d1[k])
#simplicity item
for k,v in d1.items():
    print(k+':'+v)
print(list(d1.items()))