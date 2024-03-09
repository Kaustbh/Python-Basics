dict={"Kaustubh":"Human Being",
       "Spoon": "Object"}

print(dict)

info={"name":"Karan","age":19,"eligible":True}

# print(info["name2"]) # gives error 
print(info.get("name2"))        # gives none if the value is not present 

print(info.values())

print(info.items())

for key,vlaue in info.items():
    print('Key -> {0}, Value -> {1}'.format(key,vlaue))

ep1={123:45, 224:35, 124:99}
ep2={331:23, 445:31, 222:89}

ep1.update(ep2)
print(ep1)

ep1.pop(224)
print(ep1)

ep1.popitem() # pops last element

del ep1[331]
print(ep1)