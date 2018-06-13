try:
    num = input("Number?")
    num = int(num)
    if num < 0:
        raise ValueError
except(NameError, ImportError):
    print("something went wrong")
except ValueError:
    print("Number cannot be negative.....")
finally:
    print("done")