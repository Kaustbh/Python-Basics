def average(a,b,c=1):

    print("The average is :",(a+b+c)/2)

# average(5,4)

def average(*numbers):
    print(type(numbers))
    sum=0

    for i in numbers:
        sum=sum+i
    
    print("The average is :", sum/len(numbers))

average(5,4)

def name(**name):  # takes input as dictonary 
    print(type(name))

    print("Hello",name["fname"],name["mname"],name["lname"])

name(mname="Suvalal",fname="Kaustubh",lname="Desale")