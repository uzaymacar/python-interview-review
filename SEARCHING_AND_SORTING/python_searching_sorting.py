# In Binary Search, we make use of the middle element and whether it 
# it is bigger or smaller than the target value. (and move on recursively.)
# Remember that this approach works only when the list/array is SORTED!

# The worst case scenario can be simulated by picking a value that is larger
# than the last element, and so any other element in that matter, and when
# you have a case with even elements, pick the lower element as the pivot.

# IN COMPUTER SCIENCE, ALWAYS ASSUME THAT THE LOGARITHM'S BASE IS 2!
# (unlike in math where it is usually 10)

# Binary Search has O(log(n)) efficiency (time-complexity)

# Python lists have a method called index(), which just does a search and returns 
# the first index with an instance of that value with O(n). A binary search function 
# has the same result, but searches faster, given that elements are in increasing order.

# BINARY SEARCH IMPLEMENTATION (recursive)
def binary_search_recursive(input_array, value, low, high):
    if (low > high): #error
        return -1    
    mid = (low + high)//2
    if value > input_array[mid]:
        return binary_search_recursive(input_array, value, mid + 1, high) # don't forget the return statements with recursives in Python.
    elif value < input_array[mid]:
        return binary_search_recursive(input_array, value, low, mid - 1)
    else:
        return mid

# BINARY SEARCH IMPLEMENTATION (iterative):
def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1 # take high as len - 1 in binary search!
    while low <= high:
        mid = int((high + low)/2)
        if input_array[mid] > value:
            high = mid - 1
        elif input_array[mid] < value:
            low = mid + 1
        else:
            return mid
    return -1

test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search_recursive(test_list, test_val1, 0, len(test_list) - 1))
print(binary_search_recursive(test_list, test_val2, 0, len(test_list) - 1))


# RECURSION IMPLEMENTATION (O(2^n) runtime complexity)
def get_fib(position):
    if position <= 0:
        return 0
    elif position == 1:
        return 1       
    return get_fib(position - 1) + get_fib(position - 2)

# You may have noticed that this solution will compute the values of some 
# inputs more than once. For example get_fib(4) calls get_fib(3) and get_fib(2), 
# get_fib(3) calls get_fib(2) and get_fib(1) etc. The number of recursive calls 
# grows exponentially with n. Specifically: f(1) is 2^1 steps, f(2) is 2^2 steps,
# f(3) is 2^3 steps, and f(4) is 2^4 steps. This yields 2^1 + 2^2 + 2^3 + 2^4 + ... 2^n
# runtime complexity which equals O(2^(n+1)) ~ O(2^n). This is a terrible algorithm.

print(get_fib(6))

# In practice, if we were to use recursion to solve this problem we should use a 
# hash table to store and fetch previously calculated results. 
# This will increase the space needed (space-complexity) but will 
# drastically improve the runtime efficiency. This method is called memoization.
    
# RECURSION IMPLEMENTATION WITH MEMOIZATION (O(N) runtime complexity)
# Memoization is sometimes called top-down dynamic programming.

def all_fib(position):
    memo = [0] * (position)
    for i in range(position):
        print("index " + str(i) + " : " + str(get_fib_memo(i, memo)))
        
def get_fib_memo(position, memo):
    if position <= 0:
        return 0
    elif position == 1:
        return 1
    elif memo[position] > 0:
        return memo[position]
    
    memo[position] = get_fib_memo(position-1, memo) + get_fib_memo(position-2, memo)
    return memo[position]
  
all_fib(7)

# RECURSION IMPLEMENTATION WITH BOTTOM-UP DYNAMIC PROGRAMMING (O(N) runtime complexity)
# Think about doing the same recursive memoized approach, but in reverse

def fib_bottom_up(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    memo = [0] * position
    memo[0] = 0
    memo[1] = 1
    for i in range(2, position):
        memo[i] = memo[i - 1] + memo[i - 2]
    
    return memo[position - 1] + memo[position - 2]

# Looking above, we can see that we only use memo[i] for memo[i - 1] and memo[i - 2]
# and we don't really need it after that. We can thus get rid of the memo "cache" and just use variables!

def fib_without_cache_bottom_up(position):
    if position == 0:
        return 0
    a = 0
    b = 1
    c = 0
    for i in range(2, position):
        c = a + b
        a = b # set a to b
        b = c # set b to c (a + b), this way we will store the total sum at c
    
    return a + b # to understand why we return a + b, give some values and test CAREFULLY
    

# fib(0) -> return 0, fib(1) -> return 1, fib(2) -> [fib(1) -> return 1] [fib(0) -> return 0] [store (0+1) at memo[2]], ...
# Since a constant amount of work is done N times with the above fibonacci method with memoization,
# the runtime complexity is O(n) which is a huge improvement from the previous exponential runtime.

# In Python, the Dictionary data types represent the implementation of hash tables. 
# The Keys in the dictionary satisfy the following requirements.
# 1)The keys of the dictionary are hashable i.e. they are generated by hashing 
# function which generates unique result for each unique value supplied to the hash function.
# 2)The order of data elements in a dictionary is not fixed. 
# Check folder, 'hash table web archive', for details.

    
# BUBBLE SORT IMPLEMENTATION ( time: O(N^2), space: O(1))
def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1): # start at the end, continue to the beginning until array is sorted
        for i in range(passnum): # until it hits the limit (passnum), continue checking and swapping elements one by one
            if alist[i] > alist[i+1]: # if left > right, swap
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)

# SHORT BUBBLE SORT IMPLEMENTATION (exit when array is already sorted)
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1 # as previous, start with passnum at the end index
    while passnum > 0 and exchanges: # if no exchanges on the previous iteration, then no need 
       exchanges = False
       for i in range(passnum):
           if alist[i] > alist[i+1]: # if left > right, set exchanges to True and swap
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1 # to simulate the outer loop in the previous bubble sort

alist=[20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist)
print(alist)

# MERGE SORT IMPLEMENTATION ( time: O(N*log(N), space: O(N^2))
def mergeSort(arr):
    print("Splitting ", arr)
    if len(arr) > 1:
        mid = len(arr)//2 # get mid point
        lefthalf = arr[:mid] # split the array to two halves: left,
        righthalf = arr[mid:] # and right

        mergeSort(lefthalf) # recursively sort each half: left,
        mergeSort(righthalf) # and right

        i = 0 # lefthalf iterator
        j = 0 # righthalf iterator
        k = 0 # general loop iterator, sets the output array indexes accordingly
        while i < len(lefthalf) and j < len(righthalf): # check if half iterators don't exceed the length of their halves
            if lefthalf[i] < righthalf[j]: # if lefthalf value bigger than right half value at index i
                arr[k] = lefthalf[i] # set index k in output array to the leftmark value
                i = i+1 # increment lefthalf iterator
            else: # if righthalf value is bigger or they are equal
                arr[k] = righthalf[j] # set index k in output array to the rightmark value
                j = j+1 # increment righthalf iterator
            k = k+1 # increment general loop iterator

        # reaching mere means that either lefthalf or rightmark iterator has exceeded len(half)
        # the remaining values have to be the largest either if on the left or on the right
        while i < len(lefthalf): # go over the lefthalf to see if any index is unvisited
            arr[k] = lefthalf[i] # set index k in output array to the unvisited leftmark value
            i = i+1 # increment lefthalf iterator
            k = k+1 # increment general loop iterator

        while j < len(righthalf): # go over the righthalf to see if any index is unvisited
            arr[k] = righthalf[j] # set index k in output array to the unvisited rightmark value
            j = j+1 # increment righthalf iterator
            k = k+1 # increment general loop iterator
    print("Merging ", arr)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)

# If we know that a list is nearly sorted, quick sort will be a bad approach.
# https://visualgo.net/en/sorting?slide=1 is a good website to go to visualize sorting algorithms.

# QUICK SORT IMPLEMENTATION (time: O(N log(N) on average but O(N^2) on worst case, space: O(log(N)))
def quickSort(arr):
   quickSortHelper(arr, 0, len(arr) - 1) # start with low = left = 0, high = right = len(arr) - 1

def quickSortHelper(arr, left, right):
    split_point = partition(arr, left, right) # get a split_point so that you can split the array into two halves
    if (left < split_point - 1): # sort left half
        quickSortHelper(arr, left, split_point - 1)
    if (right > split_point): #sort right half
        quickSortHelper(arr, split_point, right)

def partition(arr, left, right):
   pivot_value = arr[int((left+right)/2)] # pick pivot point, since this partitioned pivot value is
                                          # not guarenteed to be median, we have O(N^2) runtime worst case
   
   while left <= right:
       while arr[left] < pivot_value: # find element on the left that should be on the right
           left += 1 

       while arr[right] > pivot_value: # find element on the rigth that should be on the left
           right -= 1

       if left <= right: # swap elements and move left and right indices
           temp = arr[left]
           arr[left] = arr[right]
           arr[right] = temp
           left += 1 # move one past the swapped elements
           right -= 1

   return left

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)

# RADIX (BUCKET) SORT IMPLEMENTATION (time: O(k * N) where k is the number of passes of the sorting algorithm)
# This algorithm only sorts NUMBERS!

def countSort(arr, exp): # counting sorting method 
    count = [0] * (10) # initialize count array as 0
    output = [0] * (len(arr)) # initialize output array that will have elements sorted
    
    # store count of occurrences in count[]
    for i in range(len(arr)):
        index = (arr[i] / exp) 
        count[int((index) % 10)] += 1 # smart way to get digits
        
    # change count[i] so that count[i] now contains actual
    # position of this digit in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    # build the output array
    i = len(arr) - 1
    while i >= 0:
        index = int(arr[i]/exp)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1
    
    return output

def radixSort(arr):
    # find the maximum number to know max number of digits
    max_val = max(arr)
    
    output = arr # output array start as original
    
    # do counting sort for every digit
    # instead of passing digit number, exp is passed
    # exp is 10^i where i is the current digit number
    exp = 1 # one's digit
    while int(max_val/exp) > 0:
        output = countSort(output, exp)
        exp *= 10
    return output
     
print(radixSort([1, 4, 146, 25, 7, 53, 2211]))
#radixSort([1, 4, 146, 25, 7, 53, 2211])   
