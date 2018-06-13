a = 19


def test():
    global a
    b = 100
    a = a + 1
    print(a)


test()
# print(b) will give error as b is  local variable and scope of it is in within the function it has been defined

print("--------------------------------------------------------")
print("DOCUMENTATION STRING FORMAT")


def add(c, d):
        """

        :param c:
        :param d:
        :return:
        """
        return c + d


print(add.__doc__)

add(1, 2)

print("-----------------------------------------")

