# . Write a Python function to multiply all the numbers in a
#  list.
#  Sample List : (8, 2, 3, -1, 7)
#  Expected Output : -336

def multiply(nums):
    total=1
    for x in nums:
        total*=x
    return total
print(multiply((8, 2, 3, -1, 7)))