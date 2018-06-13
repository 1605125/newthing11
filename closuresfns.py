def func1(a):
    def func2(b):
        return a + b
    return func2
data = func1(100)
print(data(100))


print("-------------------------------------------------")


def func1(a):
    def func2(b):
        return "i am function 2"
    def func3(c):
        return "i am function 3"
    return [func2,func3]# form of list


data = func1(100)  #  depends on which function i am returning
print(data[0](100))# therefore we use index
print(data[1](200)) # calling function three using its index i.e is one
