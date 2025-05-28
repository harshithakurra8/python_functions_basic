# Write a Python program to count the number 4 in a given list.

def count_fours(numbers):
    return numbers.count(4)

list=[1,3,4,6,4,7,2,4,9]
count=count_fours(list)
print("The no of 4's in the list is:",count)