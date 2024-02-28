tup =(1,3,5,6,7,"Kaustubh",True)
print(type(tup),tup)

t1=(1,) # t1=(1)
print(type(t1))

print(tup[0])
print(tup[2])
print(tup[6])

if True in tup:
    print("Yes")

print(tup[1:5])

couteries=("Spain","Italy","Japan","England","Germany")
temp=list(couteries)
temp.append("India")
print(temp)
temp.pop(2)
couteries=tuple(temp)
temp=tuple(temp)
print(couteries)

t1=temp+couteries
print(t1)

print(tup.index(5))
print(tup.count(5))
print("-----------")
print(tup.index("Kaustubh",4,7,))

print("My name is \'Kaustubh\" ")

