#list = [4,5,34,5,6,8,9,20,27]

def bubble_sort(arr):
    for n in range(0,-(len(arr) -1)):
        swapped=False
        for i in range(n):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped=True
        if not swapped:
                break
arr=[4,5,34,5,6,8,9,20,27]
print("Unsorted List is:")
print(arr)

bubble_sort(arr)

print("Sorted list:")
print(arr)