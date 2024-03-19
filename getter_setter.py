class myclass:

    def __init__(self,value):
        self._value=value
    
    def show(self):
        print(f"Value is {self._value}")
    
    # Getter 
    @property  
    def ten_value(self):
        return 10*self._value
    
    # Setter
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value


obj=myclass(10)
print(obj.ten_value)

obj.ten_value=20

print(obj.show())
print(obj.ten_value)