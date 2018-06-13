def addition(name,email):
    return "Name: {0}\nEmail:{1}".format(name,email)
temp = addition(email='rajemail.com',name='Raj')
print(temp)
print("------------------------------------------------------")
# single * and double ** arguments and keywords
def sub(*args):
    print(args)
sub(1,2,3,4)
print("--------------------------------------------------------")
# ** calling to dictionary
def hello(*args,**a):
    print(a)
    print(args)
hello(1,2,3,email='rajemail.com',name='Raj')