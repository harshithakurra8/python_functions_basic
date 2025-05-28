#  Write a Python program to check whether variable is of
#  integer or string

def test(n):
    if type(n)==int:
        return "It is an integer"
    else:
        return "It is a string"
    
print(test(12))
print(test('123'))