#  Write a Python function that accepts a string and
#  calculate the number of upper case letters and lower case
#  letters.
#  Sample String : 'The quick Brow Fox'
#  Expected Output :
#  No. of Upper case characters : 3
#  No. of Lower case Characters : 12

def count_case_letters(s):
    upper_count = 0
    lower_count = 0

    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print("No. of Upper case characters:", upper_count)
    print("No. of Lower case characters:", lower_count)

s = 'The quick Brow Fox'
count_case_letters(s)
