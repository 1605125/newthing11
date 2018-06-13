# lambda expressions or lambda functions or ananoymous function
def test(a,b):
    if a> b:
        return "a is largest"
    else:
        return " b i s largest"


large = test(10,20)
print(large)


print("----------------LAMBDA EXPRESSION-------------------------")
# exp ? value1 : value2
data = lambda a,b: 'a is largest' if a > b else 'b is largest'

print(data(101,20))