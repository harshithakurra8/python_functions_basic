#  Write a Python function to find a distinct pair of
#  numbers whose product is odd from a sequence of integer
#  values

def find_odd_product_pair(numbers):
    odd_numbers=[]
    for num in numbers:
        if num % 2 == 1:
            odd_numbers.append(num)
            if len(odd_numbers)>=2:
                return odd_numbers[0],odd_numbers[1]
            
    return None
nums=[2, 3, 4, 5, 8]
result=find_odd_product_pair(nums)
if result:
    print("Found Pair:",result)
    print("Product:",result[0]*result[1])
else:
    print("No odd product pair found")