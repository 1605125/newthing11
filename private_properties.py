class A:

    def __init__(self):
        self.name = "xyz"
        self.__email = "xyz@gmail.com"  # private variable

    def __display(self):
        return "Name:{0}\nEmail:{1}\n".format(self.name, self.__email)

    def getEmail(self):
        return self.__display()


a = A()
print(a.name)
print(a.getEmail())
