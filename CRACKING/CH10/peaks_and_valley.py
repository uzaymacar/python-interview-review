def peak_valley_sorter_suboptimal(arr): # O(N log(N))
    sorted_arr = sorted(arr) # first sort the array
    for i in range(1, len(arr), 2): # after being sorted, this approach will ALWAYS work
        sorted_arr = swap(sorted_arr, i-1, i) # swap elements every two iterations
    return sorted_arr

# WHY IT WORKS: when ordered it will be like this: small <= medium <= large
# swapping these elements (i - 1 with i) will yield: medium <= small <= large 
# where medium is a valley and small is a peak, then i+=2 and repeat!
    
def peak_valley_sorter_optimal(arr): # O(N)
    output = arr
    for i in range(1, len(arr), 2):
        biggest_index = max_index(arr, i - 1, i, i + 1)
        if i != biggest_index:
            output = swap(output, i, biggest_index)
    return output
            
def max_index(arr, a, b, c):
    index_arr = [a, b, c]
    value_arr = []
    
    for index in index_arr:
        if index >= 0 and index < len(arr):
            value_arr.append(arr[index])
        else:
            value_arr.append(-1024)
    
    max_value = max(value_arr)
    print(max_value)
    print(value_arr[0], value_arr[1], value_arr[2])
    print(a, b, c)
    print("---------------------------------------")
    if max_value == value_arr[0]:
        return a
    elif max_value == value_arr[1]:
        return b
    else:
        return c
    
def swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    return arr

print(peak_valley_sorter_optimal([0, 1, 4, 7, 8, 9]))