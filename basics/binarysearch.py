'''
Simple binary search algorithm, where in a sorted array searching
for an element is O(logn). 
'''

def bin_search(arr, target):

    n = len(arr)

    if n == 0:
        return -1
        
    val = arr[n//2]

    if val == target:
        return n // 2
    elif val > target:
        # Repeat on the left half
        bin_search(arr[0:(n//2)], target)
    elif val < target:
        # Repeat on the right half
        return n//2 + bin_search(arr[(n//2)+1:], target)
    else:
        return -1