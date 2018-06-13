str1 = "this is\tstring example....wow!!!";

print("Original string: " + str1)
print("Defualt exapanded tab: " + str1.expandtabs())
print("Double exapanded tab: " + str1.expandtabs(16))
name="raju"
email="raju@gmail.com"
age=22
name="Name:{0}\nEmail:{1}".format(name,email)
print(name)
name="Name: %s\nEmail:%s\nAge:%d"%(name,email,age)
print(name)
name="Name:"+name+"\nEmail:"+email+"\nAge :"+str(age)
print(name)
'''
item_one=1
item_two=2
item_three=3
total = item_one + \
        item_two + \
        item_three
print(total)
'''
