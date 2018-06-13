class A:
#     def __init__(self):
#         print("I am init of class A")
#         self.name = 'Raj'
#         self.email = 'raj@gmail.com'
    def __init__(self, name, email):
        print("I am init of class A")
        self.name = name
        self.email = email

    def display(self):
        return self.name + "\n" + self.email

    def __del__(self):
        print("i am here")

    def __str__(self):  # will change value of object as alias
        return self.name


# a = A()  # constructor gets invoked
a = A("raj", "raj@gmail.com")
temp = a.display()

print(temp)
print(hasattr(a, 'name1'))
print(a)
