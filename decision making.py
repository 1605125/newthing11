a=13
if a==10 :
    print("A: {0}".format(a))
elif a==12:
    print("A: {0}".format(a))
elif a==13:
    print("A: {0}".format(a))
else:
    print("else block")
# nested if
a1=10
b=11
c=122
if(a1==10):
    if(b==11):
        if(c==12):
            print("Done")
        else:
            print("Failed at c check point")
    else:
        print("failed at B check point")
else:
    print("failed at A check point")


