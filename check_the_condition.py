#  Write a Python program that will return true if the two
#  given integer values are equal or their sum or difference is
#  5

def check_numbers(a, b):
    if a ==b:
        return True
    elif a+b==5:
        return True
    elif a-b==5:
        return True
    else:
        return False
    
a = int(input("Enter 1st no:"))
b = int(input("Enter 2nd no:"))

result =check_numbers(a,b)
print("Result",result)