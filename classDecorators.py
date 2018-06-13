# static method
class A:

    def __init__(self):
        self.name = "xyz"
        self.__email = "xyz@gmail.com"  # private variable

    @staticmethod
    def dosmthng(a, b):  # self becomes user define parameter
        print("i am in dosmthng function!")
        print(a+b)


a = A()
a.dosmthng(1, 3)

print("\n==================class method===================")
# class method


class B:
    def __init__(self, nam, addr):
        self.nam = nam
        self.addr = addr


    @classmethod
    def smthngdo(cls):
        a2 = cls("abc", "btm")
        print(a2.nam)
        print(a2.addr)


mm = B('csk', 'bangalore')
mm.smthngdo()
print("=========outside class=======")
print(mm.nam)
print(mm.addr)


