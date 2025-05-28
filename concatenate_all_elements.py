#  Write a Python program to concatenate all elements in a
#  list into a string and return it

def concatenate_all_list(lst):
    return "".join(str(element)for element in lst)

list = [1,"hello",5.22,False]
result=concatenate_all_list(list)
print("Concatenate String:",result)