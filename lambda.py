double = lambda x: x*2

cube = lambda x: x**3

avg = lambda x,y: (x+y)/2


def appl(fx,value):

    return 6+ fx(value)


print(double(5))
print(cube(2))
print(avg(5,4))

print(appl(lambda x: x**3,2))