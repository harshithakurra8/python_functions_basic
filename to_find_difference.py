# 16. Write a Python program to get the difference between a
 #given number and 17, if the number is greater than 17 return
 #double the absolute difference.

def difference(num):
    if num > 17:
        return abs(num - 17) * 2
    else:
        return abs(17 - num)
    
num=int(input("Enter a number: "))
print("The difference is:", difference(num))