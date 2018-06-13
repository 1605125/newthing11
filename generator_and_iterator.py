def testGen():
    # yield 1
    # yield 2
    # yield 3
    # yield 'xyz'
    # no need of  any return statements as generator function no return type
    # for inside yield
    for i in range(1,11):
        yield i*i


temp = testGen()
# print(temp.__next__())
# print(temp.__next__())
# print(temp.__next__())   "Bad approach"
try:
    while True:
        print(temp.__next__(), end='  ')

except:
    pass   # function  with no body is passed

