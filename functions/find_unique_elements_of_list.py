#  Write a Python function that takes a list and returns a
#  new list with unique elements of the first list.
#  Sample List : [1,2,3,3,3,3,4,5]
#  Unique List : [1, 2, 3, 4, 5]

def unique_list(l):
    x=[]
    for a in l:
        if not a in x:
            x.append(a)
    return x
print(unique_list([1, 2, 3, 3, 4, 3, 5]))