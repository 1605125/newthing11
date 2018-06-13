def email(funName):
    def executeDemo():
        print("i am in email Decorator")
        funName()

    return executeDemo

@email
def name():
    print("Raj")

name()
