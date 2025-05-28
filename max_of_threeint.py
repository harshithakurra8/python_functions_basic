#  Write a Python function to find the Max of three numbers

def max_if_three_num(a, b, c):
    # return max( a, b, c)
    if a>=b and a>=c:
        return a
    if b>=c and b>=a:
        return b
    else:
        return c
        
print(max_if_three_num(10,57,55))