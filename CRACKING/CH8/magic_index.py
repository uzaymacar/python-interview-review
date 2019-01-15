# Whenever you see sorted in a question, think about Binary Search (O(log(N)))
# This is because you are never given extra information, every information is given for a reason!

def magic_helper(arr):
    return magic_index(arr, 0)
    
def magic_index(arr, pos):
    if arr[pos] == pos:
        return pos
    return magic_index(arr, pos + 1)
        
def magic_dumb(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i

def magic_bin_search_helper(arr):
    # return magic_bin_search(arr, 0, len(arr) - 1) # dont forget to return!!!
    return magic_bin_search_not_distinct(arr, 0, len(arr) - 1)
def magic_bin_search(arr, low, high): # this only works when the elements are distinct
    mid = int((low + high)/2)
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return magic_bin_search(arr, low, mid - 1)
    elif arr[mid] < mid:
        return magic_bin_search(arr, mid + 1, high)

def magic_bin_search_not_distinct(arr, low, high): # works with all cases, to see this write it out all!
    if low > high:
        return -1 # not found!
    mid = int((low + high)/2)
    
    if arr[mid] == mid:
        return mid
    
    left = magic_bin_search_not_distinct(arr, low, min(arr[mid], mid - 1))
    if left > 0:
        return left
    
    right = magic_bin_search_not_distinct(arr, max(arr[mid], mid + 1), high)
    if right > 0:
        return right
    
    return -1
       
print(magic_bin_search_helper([-5, -2, 0, 0, 1, 4, 6])) # to come from behind, you can give negative values like this
