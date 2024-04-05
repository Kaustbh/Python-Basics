
# dir 

x=[1,2,3,4,5]
print(dir(x),end="\n \n")

print(type(x.append),end="\n \n")

print(type(x.__add__))

print("-----------------------------------------")

# dict 

class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1.0

    def show(self):
        pass

p=Person("Kaustubh",21)
print(p.__dict__) # give all the variables in the class in dictonary format .

# help 

print(help(Person))
# print(help(list))