def get_index_in_rotated(arr, element):
    return binary_search(arr, 0, len(arr) - 1, element)
    
def binary_search(a, low, high, x):
    mid = (low+high)//2
    
    if x == a[mid]:
        return mid
     
    if (low > high):
        return -1 
    
    # either the left or right half must be normally ordered.
    # find out which side is normally ordered, then use normally ordered half
    # to figure out which side to search to find x
    
    if a[low] < a[mid]: # left is normally ordered
        if x >= a[low] and x < a[mid]:
            return binary_search(a, low, mid - 1, x) # search left
        else:
            return binary_search(a, mid + 1, high, x) # search right
    
    elif a[mid] < a[low]: # right is normally ordered
        if x > a[mid] and x <= a[high]:
            return binary_search(a, mid + 1, high, x) # search right
        else:
            return binary_search(a, low, mid - 1, x) # search left
    elif a[low] == a[mid]: # left or right half is all repeats
        if a[mid] != a[high]: # if right is different, search it
            return binary_search(a, mid + 1, high, x) # search right
        else: # else, we have to search both values
            result = binary_search(a, low, mid - 1, x) # search left
            if result == -1:
                return binary_search(a, mid + 1, high, x) # search right
            else:
                return result
                
ar = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
el = 5

print(get_index_in_rotated(ar, el))