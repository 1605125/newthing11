
try:
    int("sds")
    name = 'aaasdfn'
    print(name)
    import sdfdedd
    print("went good")
except(NameError,ValueError,ImportError):   # handling multiple error in one time
    print("Something went wrong")
except IOError:
    print("Exception")
except ImportError:
    print("ImportError")
except NameError:
    print("NameError")
except ValueError:
    print("value exception")

finally:
    print("I a always here")
