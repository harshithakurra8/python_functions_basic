# . Write a Python function to find the maximum and minimum
#  numbers from a sequence of numbers.
#  Note: Do not use built-in functions

def max_min(data):
    l=data[0]
    s=data[0]
    for num in data:
        if num > l:
            l = num
        elif num < s:
            s = num
    return l , s
print(max_min([2, 19, 57 ,22 , -3]))