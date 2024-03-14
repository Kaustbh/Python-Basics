def cube(x):

    return x**3
  

# MAP 

l=(1,2,3,4,5) # can be list also 

newl=map(cube,l)
print(newl)

newl=tuple(map(cube,l)) # convert it to your desired dtype

# using lambda function 
newl2=tuple(map(lambda x: x**3, l))

print(newl)
print(newl2)

print("---------------------------")

# FILTER

def filter_fun(x):

    return x>2

newl=list(filter(lambda x: x>2,l))
print(newl)

print("--------------------------------------")

# REDUCE

# we have to first import reduce 

from functools import reduce

def mysum(x,y):
    
    print(f'x -> {x}, y -> {y} ')
    return x+y

sum = reduce(mysum,l)
# sum = reduce(lambda x,y: x+y, l)
print(sum)

