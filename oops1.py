class Person:

    def __init__(self,n,o) -> None:
        
        print("I am a constructor")
        self.name=n
        self.occupation=o
        
    def info(self):

        print(f'{self.name} is a {self.occupation}')


a=Person("Kaus","Developer")


a.info()
