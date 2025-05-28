#  Write a Python program to sum of all counts in a
#  collections

import collections
nums=[2, 3, 2, 4, 5, 3, 8, 4]
result=sum(collections.Counter(nums).values())
print(result)