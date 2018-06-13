d1={'name':'Raju',
    'email':'raju@gmail.com',
    'city':'bangalore',
    'phone':'7993231908'
}
# item function
for k, v in d1.items():
    print(d1[k])
# without item function
for k in d1:
    print(d1[k])    # displays values
for k in d1:
    print(k)    # displays key
# simplicity item
for k, v in d1.items():
    print(k+':'+v)
print(list(d1.items()))