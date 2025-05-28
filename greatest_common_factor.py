# . Write a Python program to compute the greatest common
#  divisor (GCD) of two positive integers

def compute_gcd(x,y):
    while y:
        x, y = y, x % y
    return x

num1 = int(input("Enter first positive number:"))
num2 = int(input("Enter second positive number:"))

gcd = compute_gcd(num1,num2)
print("The GCD of ",num1, "and" ,num2,"is:",gcd )