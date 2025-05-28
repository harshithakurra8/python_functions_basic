# Write a Python program to create a histogram from a given
 #list of integers
def histogram(numbers):
    for num in numbers:
        print('*'*num)

list=[4,2,7,2,8,4]
print("Histogram:")
histogram(list)