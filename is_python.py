a=4
b="4"

print(a is b ) # checks exact location of the object in memory (identity)
print(a == b, end='\n')  # compares values 

a= "kaustubh"
b= "kaustubh"

print(a is b) # True for immutable objects like , constants, strings , tuples etc
print(a == b,end='\n')  # compares values in case of list , tuples etc

a= (1,2,4,5)
b= (1,2,4,5)

print(a is b) 
print(a == b,end='\n') 