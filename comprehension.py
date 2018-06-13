def sqr(l1):
    temp = []
    for i in l1:
        temp.append(i*i)
    print(temp)


listData1 = [1, 2, 3, 4, 5]
sqr(listData1)



print("--------------Comprehension concept-----------------------")
# Expression for varname in sequence condition
data1 = [i*i for i in listData1]
print(list(data1))
evendata2 = [i*i for i in listData1 if i % 2 == 0]  # with condition
print("even data {}" .format(list(evendata2)))
print("expression type")
listData2 = [6, 7, 8, 9, 10]
l2 = [10, 20]
datamul = [i*j for i in listData2 for j in l2 if i%2 == 0]
print("multiplied {}".format(list(datamul)))


print("----------------dictionary cpmprehension-----------------")
dicdata = {i: i*i for i in listData1}
print(dicdata)
