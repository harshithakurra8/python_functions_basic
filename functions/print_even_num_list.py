#  Write a Python program to print the even numbers from a
#  given list.
#  Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#  Expected Result : [2, 4, 6, 8]

def get_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = get_even_numbers(sample_list)

print("Even numbers:", result)
