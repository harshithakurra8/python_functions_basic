#  Write a Python program to get the least common multiple
#  (LCM) of two positive integers

def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def compute_lcm(x, y):
    return(x * y)//compute_gcd(x , y)

num1=int(input("Enter the first positive no:"))
num2=int(input("Enter the second positive no:"))

lcm=compute_lcm(num1, num2)
print("The LCM of",num1 ,"and", num2, "is:",lcm )