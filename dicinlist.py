#list in tuple and tuple in list
l1=[1,2,3,4]
l1.append({'name':'raj','email':'raj@gmail.com'})
l1[4].update({'city':'bangalore'})
print(l1)
#nested list
l1.append([100,200,300])
print(l1)
l1[5].append(400)
l1.append([91000,3000])
print(l1)
print(l1[6])
print(l1[6][0])