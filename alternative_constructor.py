class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def show_details(self):
        pass

    @classmethod
    def fromstr(cls,str):
        return cls(str.split("-")[0],int(str.split("-")[1]))
    


e1=Employee("Harry",100000)
s="Kaustubh-100000"
e2=Employee.fromstr(s)
print(e2.name)
print(e2.salary)


class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @classmethod
    def from_string(cls,str):
        name,age=str.split(",")
        return cls(name,int(age))

p1=Person.from_string("John Doe,30")
print(p1.name)
print(p1.age)

