class A:
    def __init__(self, a):
        self.a = a

    def getA(self):
        return self.a

    def display(self):
        return "A:{0}\n".format(self.a)


class B:
    def __init__(self, b):
        self.b = b

    def getB(self):
        return self.b


class C(A, B):
    def __init__(self, a, b, c):
        # super(C, self).__init__(a)  only class A constructor will be called
        A.__init__(self, a)     # multiple inheritance pattern
        B.__init__(self, b)
        self.c = c

    def getC(self):
        return self.c

    def display(self):
        return "A:{0}\nB:{1}\nC:{2}\n".format(self.a, self.b, self.c)


c = C(1, 2, 3)
temp = c.display()
print(temp)



