ll=[3,5,"Kaustubh",True]
print(type(ll))
print(ll[0])
print(ll[3])

print(ll[-3]) # print(ll[len(ll)-3])

if "Kaustubh" in ll:

    print("Yes")
else:
    print("No")


if "aust" in "Kaustubh":
    print("Yes")

print(ll[1:-1])

# list comprehension 

ll=[i*i for i in range(10) if i%2==0]

print(ll)

ll=[3,5,4,6,44,74,23]
ll.append(45)
ll.sort()
ll.sort(reverse=True)

print(ll)
print("-------------")

print(ll.index(4))
print(ll.count(4))

ll.reverse()
print(ll)

m=ll
m[0]=0
print(m)
print(ll)

m=ll.copy()
m[0]=5
print(m)

m.insert(1,100)

m=[100,300,900]
# ll.append(m)
ll.extend(m)
print(ll)

k=ll+m
print(k)

print("--------------------------------------------------------")

a=[1,23,45,21,67,98,34,56]

for index , mark in enumerate(a):

    print(mark)
    if index==5:
        print("Awesome!")

for index , mark in enumerate(a,start=2):

    print(index,mark)

import numpy

# print(dir(numpy))

print("-----------------------------------------------------")

# from temp import welcome,kaus
# from temp import *

# welcome()
# print(kaus)

print("------------------------------------------------------")


import temp

temp.welcome()

