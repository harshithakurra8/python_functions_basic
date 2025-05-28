#  Write a Python program to get the n (non-negative
#  integer) copies of the first 2 characters of a given string.
#  Return the n copies of the whole string if the length is less
#  than 2

def get_copies(str,n):
    if len(str)<2:
        return str*n
    else:
        return str[:2]*n
    
print(get_copies("python",3))
print(get_copies("Hi",2))