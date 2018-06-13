class A:

    def add(self):  # self refers to current object behaves like this of java
        return "I am in add function of class A"

    def sub(self):
        return "I am in sub function of class A"


a = A()
temp = a.sub()
print(temp)
temp2 = a.add()
print(temp2)

print("\n---------------user info------------------------")


class UserInfo:

    def setInfo(self, name, email):
        self.name = name
        self.email = email

    def getInfo(self):
        return "name: {0}\nemail: {1}".format(self.name, self.email)


userObj = UserInfo()
print("===========user1================")
userObj.setInfo("Raju", "Raju@gmail.com")
tem = userObj.getInfo()
print(tem)
print("============user2===============")
userObj2 = UserInfo()
userObj2.name = "megha"
userObj2.email = "meghamaggi091@gmail.com"
tem = userObj2.getInfo()
print(tem)
# both have different space

