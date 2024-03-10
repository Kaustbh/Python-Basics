# a=input("Enter the number: ")
# print(f"Multiplication table of {a} is :")


# try:
#     for i in range(1,11):

#         print(f"{int(a)} X {i} = {int(a)*i}")

# except Exception as e:
#     # print(e)
#     print("Invalid Input !")

# print("Some important lines of code")

# try:
#     num=int(input("Enter an integer: "))
#     a=[10,15]
#     print(a[num])

# except ValueError:
#     print("Number entered is not an integer")

# except IndexError:
#     print("Index Error")


print("----------------------------------------------------------------------")

# Finally Clause :

def func1():

    try:
        l=[1,4,5,6,7]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    
    except:
        print("Some error occured ")
        return 0
    
    finally: # it is executed even after the return statement 
        print("I am always executed")

x=func1()
print(x)

