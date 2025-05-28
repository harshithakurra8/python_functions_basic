#  Write a Python function that takes a positive integer
#  and returns the sum of the cube of all the positive integers
#  smaller than the specified number

def sum_of_cubes(n):
    if n <= 1:
        return 0
    return sum(i**3 for i in range (1,n))
print(sum_of_cubes(4))