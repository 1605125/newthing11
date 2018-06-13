class A:
    def __init__(self, a):
        self.a = a

    def getA(self):
        return self.a

    def display(self):
        return "A:{0}\n".format(self.a)


class B(A):
    def __init__(self, a, b):
        super(B, self).__init__(a)
        self.b = b

    def getB(self):
        return self.b

    def display(self):
        return "{0}\nB:{1}\n".format(super(B, self).display(), self.b)


class C(B):
    def __init__(self, a, b, c):
        super(C, self).__init__(a, b)
        self.c = c

    def getC(self):
        return self.c

    def display(self):
        return "{0}\nC:{1}\n".format(super(C, self).display(), self.c)


c = C(1, 2, 3)
temp = c.display()
print(temp)



