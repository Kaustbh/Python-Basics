# 'rt' for reading text File
# 'rb' for reading binary file

# using "with"  we dont need to close files manualy 

# with open("sample.txt",'w') as f:
#     f.write("Hi , how are you")
#     f.close()


# f=open('sample.txt','r') # 'r' is the default mode 

# text=f.read()
# print(text)
# f.close()



# f=open('sample.txt','a') # 'r' is the default mode 

# f.write("What is your name")
# f.close()


# f=open('sample.txt','r') # 'r' is the default mode 

# while True:
#     line=f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break

# f=open('sample2.txt','w')
# lines=['line1\n','line2\n','line3\n','line4\m']

# f.writelines(lines)
# f.close()


with open('sample2.txt','r') as f:
    f.seek(50) # seeks or starts reading from 50th index

    print(f.tell()) # tells the current position of the file index
    text=f.read(10)  # read 10 bytes or characters
    print(text)


