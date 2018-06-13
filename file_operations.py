file = open("fileDemo", 'w')
# file.write('hello , how are you,something1  \n')
file.writelines(['hello python\n', 'hi\n'])
print(file.writable())
file.close()

# print(file)
