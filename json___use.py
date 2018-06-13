from json import dumps, loads
dic = {'a': 1, 'b': 2, 'c': 3}
with open('dd', 'w') as f:
    f.writelines(dumps(dic))  # dictionary/list /tuple to json-string
    # f.writelines(str(dic)) will show output but we cant read it
file = open("dd")
data = file.read()
print(data[3])      # all converted to string
data = loads(data)  # brings json_string to meaningful format
print(data)
print(data["a"])    # extracted by way of dictionary
file.close()
