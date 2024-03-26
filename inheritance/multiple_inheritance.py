class Employee:

    def __init__(self,name):

        self.name=name
    
    def show(self):

        print(f"The name is {self.name}")


class Dancer:

    def __init__(self,dance):

        self.dance=dance
    
    def show(self):

        print(f"The name is {self.dance}")

class EmployeeDance(Employee,Dancer):

    def __init__(self,name,dance):

        self.name=name
        self.dance=dance
    

o=EmployeeDance("Shivani","Kathak")

o.show()
print(EmployeeDance.mro()) # Method resolution operator

