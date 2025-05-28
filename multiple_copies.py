def multiple_copies(s,n):
    if n<0:
        return "Error must be non-negative integer"
    return s*n
input_string=input("Enter the String:")
n=int(input("Enter a non-negative integer:"))
result=multiple_copies(input_string,n)
print("Result:",result)