# 25. Write a Python program to check whether a specified value
#  is contained in a group of values.
#  Test Data :
#  3 -> [1, 5, 8, 3] : True-1 -> [1, 5, 8, 3] : False

def value_in_group(value,group):
    return value in group

print("3 -> [1, 5, 8, 3] :", value_in_group(3, [1, 5, 8, 3]))
print("1 -> [1, 5, 8, 3] :", value_in_group(1, [1, 5, 8, 3]))
print("9 -> [1, 5, 8, 3] :", value_in_group(9, [1, 5, 8, 3]))