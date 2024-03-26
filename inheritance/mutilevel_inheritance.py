class Animal:

    def __init__(self,name,species):

        self.name=name 
        self.species=species
    
    def show_details(self):

        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

class Dog(Animal):

    def __init__(self,name,breed):

        Animal.__init__(self ,name,species="Dog")
        self.breed=breed
    
    def show_details(self):

        Animal.show_details(self)
        print(f"Breed : {self.breed}")

class GoldenRetriver(Dog):

    def __init__(self,name,color):

        Dog.__init__(self,name,breed="GoldenRetriver")
        self.color=color
    
    def show_details(self):
        
        Dog.show_details(self)
        print(f"Color : {self.color}")
    

o=GoldenRetriver("tommy","black")
o.show_details()
print(GoldenRetriver.mro())