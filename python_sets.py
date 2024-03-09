s={2,4,4,5}
print(s)

info ={"Hi" , 13 , 24 ,"Bye","Hi "} # doesnt maintains any order , we cant use info[0],info[2] etc
print(info)

kaus = {}
print(type(kaus))

kaus = set()
print(type(kaus))

s1={2,7,3,4,"HI"}
s2={2,3,7}
print(s1.union(s2)) # keeps in sorted order

s1.update(s2)
print(s1)

cities={"Tokyo" ,"Delhi", "Berlin"}
cities2 ={"Madrid", "Berlin" , "Kabul", "Madrid"}
cities.intersection_update(cities2)

cities={"Tokyo" ,"Delhi", "Berlin"}
print(cities,end="\n \n")
print("-------------------")
cities3=cities.symmetric_difference(cities2)
print(cities3)

cities3=cities.difference(cities2)
print(cities3)

print(cities.isdisjoint(cities2))
print(cities.issuperset(cities2))

cities.add("Helsinki")

cities.remove("Tokyo") # raises error if the element is not present in the set
#cities.remove("Tokyo2") 

cities.discard("Tokyo2")  # doesnt raise any error

cities.update(cities2)
print(cities)

item=cities.pop() # pops random element
print(cities)
print(item)


cities.clear()
print(cities)
del cities # deletes sets 