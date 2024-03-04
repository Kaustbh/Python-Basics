for i in range(5):

    print(i)

# we can use else with for and while , it executes after all iterations of the loops are completed 
else:
    print("Sorry no i ")


print("-------------------------------------")
for i in range(6):
    print(i)
    if i==4:
        break

else: # in this case else will not execute , because for loop is not completely executed it is breaked 
    print("Sorry no i")


