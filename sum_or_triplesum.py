# Write a Python program to calculate the sum of three
 #given numbers, if the values are equal then return three
 #times of their sum

def sum(a,b,c):
    total=a+b+c
    if a==b==c:
        return total*3
    else:
        return total
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

result = sum(a,b,c)
print("The result is:", result) 
