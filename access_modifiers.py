class Employee:

    def __init__(self):

        self.__name ="Kaustubh"  #  "__" is used before variables to declare them as Private .
    

e=Employee()
# print(e.__name)

# Name Mangling
print(e._Employee__name) # we can access Private variables using this convention , _(class)__(variable name)
print(e.__dir__())

class Student:

    def __init__(self):
        
        self._name="Harry"  # "__" is used before variables to declare them as Protected
    
    def _funname(self):  # Protected Function 

        return f"My name is {self._name}"

class Subject(Student):

    pass 

a=Student()
b=Subject()

print(a._name)
print(b._funname()) # we can also call functions like this ->    " Student._funname(b) "

print("----------------------------------------------")

# Static Method 

# we can call static method without creating the instance of class aslo.
 
class Math:

    def __init__(self,num):
        self.num=num
    
    def addtonum(self,n):
        self.num=self.num+n
    
    @staticmethod
    def add(a,b):
        return a+b

class Math2(Math):
    pass

o=Math(10)
o2=Math2(2)

o.addtonum(6)
print(o.num)
print(Math.add(6,8))
print(Math2.add(3,3))

print("------------------------------------------------",end="\n")

# class Method 

class Employee:
    company="Apple"
    def __init__(self):
        pass

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    @classmethod  # used to modify class variables 
    def changecompany(cls,newcompany):  # The first argument is class 
        cls.company=newcompany


e1=Employee()
e1.name="Kaustubh"
e1.show()
e1.changecompany("Tesla")

e1.show()
print(Employee.company)



 