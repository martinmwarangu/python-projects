


def recursive_binary_search(list, target, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_binary_search(list, target, start, mid-1)
        else:
            return recursive_binary_search(list, target, mid+1, end)
def verify(index):
     if index is not None:
        print("Target found at index:", index)
     else:
        print("Target not found on list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(numbers,15)   
verify(result) 
result = recursive_binary_search(numbers,7)   
verify(result) 
       