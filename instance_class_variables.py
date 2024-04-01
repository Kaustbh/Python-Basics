class Employee:
    company_name="Apple"  # class variables
    def __init__(self,name):
        self.name=name
        self.rais=0.02
    
    def show_details(self):

        print(f"The name of the Employee is {self.name} and the raise amount in {self.company_name} is {self.rais}")

    
emp1=Employee("Kaus")
# emp1.show_details() 
Employee.show_details(emp1)

emp2=Employee("Harry")
emp2.rais=0.3
emp2.show_details()


emp1.company_name="Apple India"
emp1.show_details()

Employee.company_name="Nestle"

print(Employee.company_name)

