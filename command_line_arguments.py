# #  Write a Python program to get the command-line arguments
# #  (name of the script, the number of arguments, arguments)
# #  passed to a script

# import sys

# print("This is  the name/path of the  script:"),sys.argv[0]

# print("Number of arguments:",len(sys.argv))

# print("Argument List:",str(sys.argv))

import sys
n= len(sys.argv)    
print("Total arguments passed:",n)
print("\nName of python script:",sys.argv[0])

print("\nArguments passed:", end="")
for i in range(1, n):
    print(sys.argv[i],end="")

sum=0
for i in range(1, n):
    sum+= int(sys.argv[i])
print("\n\nResult:",sum)