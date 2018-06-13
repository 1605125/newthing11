class A:
    count = 0

    def setData(self, name, counter):
        self.name = name
        A.count += 1
        self.counter = counter


a = A()
a.setData("Raj", 2)
print(a.count)
a2 = A()
a2.setData("Raju", 3)

print(a.count)
print(a2.count)
print(a.counter)
print(a2.counter)
