#  Write a Python program to sum of two given integers.
#  However, if the sum is between 15 to 20 it will return 20.

def sum(a,b):
    total=a+b
    if total>=15 and total<=20:
        return 20
    else:
        return total
    
a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))

result=sum(a,b)
print("Result",result)