class Employee:

    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showDetails(self):

        print(f"The Name of employee : {self.id} is {self.name}")
    

# Inheritance
class Programmer(Employee):
    
    # def __init__(self):

    #     print("Hi")

    def showLanguage(self):
        print("The default language is Python ")
    

e1=Employee("Kaustubh",120)
e1.showDetails()

e2=Programmer("Harry",400)
e2.showDetails()
e2.showLanguage()