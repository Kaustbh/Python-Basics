# name="Kaustubh Desale"
# print(len(name),end="\n")
# print(name[0:5],end="\n")
# print(name[:])
# print(name[:-5])
# print(name[-8:-3])
# print(name.lower())
# nam="desale!!!!!Kaustubh Desale !!!!!!!!!"
# print(nam.rstrip("!")) # strips only trailing symbols
# print(nam.replace("desale"," "))
# print(nam.split(" "))
# print(nam.capitalize()) # capitilzes only first letter to capital , and all remaning to lower case

# str1="Welcome to the Console!"

# print(str1.center(50))
# print(nam.count("!"))
# print(str1.endswith("!"))
# print(str1.endswith("Console"))
# print(str1.endswith("to",4,10))

# str1="He's name is Dan. He is an honest man."
# print(str1.find("is")) # gives index of first occurence
# print(str1.find("iss"))

# # print(str1.index("ishh")) 
# name="Kaustubh"
# print(name.isalnum()) # should be in between A-Z,a-z,0-9, also affected by space
# print(name.isalnum())
# print(name.islower())

# str1="We wish you ,Happy Holi\n"
# print(str1.isprintable())
# print(str1.isspace()) # if the string only white spaces

# str1="World Health Organization"
# print(str1.istitle())
# print(str1.startswith("World"))
# print(str1.swapcase())


# str1="He name is Dan. He is an honest man."
# print(str1.title())


print("---------------------------------------------------------------")

lett="Hey my name is {1} and I am from {0} "
country="India"
name="Kaustubh"
print(lett.format(country,name))
print(f"Hey my name is {name} and I am from {country}")


l=f"Hey my name is {name} and I am from {country}"
print(l)

txt="For only {price:.2f} dollars!"
print(txt.format(price=49.2323))

print(f"We use f-strings like this -: Hey my name is {{name}} and I am from {{country}}")

print("-----------------------------------------------------------")

def square(n):
  #  print("Hii")
    '''Takes in a number n, returns the square of n'''
    print(n**2)

square(5)

print(square.__doc__) # doc string only works if it is defined immediately after class or function definition or before function body
