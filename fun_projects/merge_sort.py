from heapq import merge


def merge_sort(list):
    """
    sorts list in ascending order
    returns sorted list 
    divide: divides list at midpoin
    conqure: recursively sorst the sublits created
    combine: merge the sublists sorted in previous step
    """
    if len(list) <=1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left,right)
def split(list):
    """
    divides the unsorted list at midpoint and then returns 
    two sublists left and right
    runs i O(logn)
    """    
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left,right
def merge(left,right):
    """
    merges two lists sorting them in the process 
    returns new list
    take O(nlogn)
    """
    l=[]
    i=0
    j=0
    while i < len(left) and j< len(right):
        if left[i] < right [j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    while i < len(left):
        l.append(left[i])
        i+=1
    while j < len(right):
        l.append(right[j])
        j+=1
    

    return   l 



def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0]<list[1] and verify_sorted(list[1:])  
blist = [25,39,27,23,48,50,65,19]
blist = [25,39,27,23,48,50,65,19]
l= merge_sort(blist)

print(verify_sorted(blist))  
print(l)     



