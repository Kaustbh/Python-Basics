# import time 

# curr_tim=time.localtime()
# t=time.strftime("%H:%M:%S",curr_tim)
# print(t)

# hr=t.split(":")[0]
# print(hr)
# hr=int(hr)
# if hr>=1 and hr<=12:
#     print("Good Morning")

# elif hr>12 and hr<=15:
#     print("Good AfterNoon")
# elif hr>=16 and hr<=18:
#     print("Good Evening")
# else:
#     print("Good Night")


# x=int(input("Enter the number: "))

# match x:

#     case 0:
#         print("x is zero")
    
#     case 4:
#         print("x is four")
    
#     case _ if x!=90:
#         print("x is not 90")
    
#     case _ if x!=80:
#         print("x is not 80")
    
#     case _:
#         print(x)

# count=5

# while (count>0):
#     print(count)
#     count=count-1

# else:
#     print("I am inside else")


# short hand if-else 
    
a=330
b=3303

print("A") if a>b else print("=") if a==b else print("B")

c=9 if a>b else 0
print(c)



 