#write program to read string from command propmt and print how many words are there
print("enter the string")
x=input()
x=x.strip()
x=x.split(" ")
length=x.__len__()
print(length)
