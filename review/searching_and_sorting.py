""" 
BINARY SEARCH

-> In binary search, we make use of the middle element, whether it 
   it is bigger or smaller than the target value, and repeat this procedure recursively

-> Remember that binary search works only when the list/array is SORTED!

-> The worst case scenario can be simulated by 
   a) searching for the lowest & greatest element if there are odd number of elements
   b) searching for the greatest element if there are even number of elements
   c) searching for an element not in the list/array

-> Can workaround worst case scenario c) by comparing the search value
   with the first and the last element, and checking if it is between
   these values before starting binary search.

-> Side Note: In C.S., always assume that a logarithm's base is 2,
   unlike in mathematics where we usually assume that the base is 10.

-> Binary search has O(log(N)) time complexity.

-> Why is useful? Python lists have a method called index(), which just does a search and 
   returns the first index with an instance of that value with O(n). A binary search function 
   has the same result, but searches faster, given that elements are in increasing order.

-> Side Note: Don't forget the return statements with recursives in Python. Or else,
   you will just return None.
   
-> Side Note: As a general rule, try to limit the usage of global variables in Python.
   This will help you prevent "local variable referenced before assignment" error
   and the unnecessary usage of the 'global' keyword.
"""

passes_recursive = 0 # counter for number of recursive binary search steps

# RECURSIVE BINARY SEARCH IMPLEMENTATION
def binary_search_recursive(input_array, value, low, high):
    global passes_recursive # not really elegant code, normally try to pass as parameter
    passes_recursive += 1 # increment counter
    
    if (low > high): # error, means search value not found
        return -1    
    mid = (low + high)//2 # cast mid to int
    if value > input_array[mid]: # if search value greater than mid value, RETURN right binary search
        return binary_search_recursive(input_array, value, mid + 1, high) 
    elif value < input_array[mid]: # if search value smaller than mid value, RETURN left binary search
        return binary_search_recursive(input_array, value, low, mid - 1)
    else: # else, search value equals mid value 
        return mid 

passes_iterative = 0 # counter for number of iterative binary search steps

# ITERATIVE BINARY SEARCH IMPLEMENTATION
def binary_search_iterative(input_array, value):
    global passes_iterative # not really elegant code, normally try to pass as parameter
    
    low = 0
    high = len(input_array) - 1 # take high as len - 1 in binary search!
    while low <= high: # continue until low is greater than high (can equal each other)
        passes_iterative += 1 # increment counter
        mid = (high + low)//2 # cast mid to int
        if value < input_array[mid]: # if search value is smaller than mid value
            high = mid - 1 # search left half
        elif value > input_array[mid]: # if search value is greater than mid value
            low = mid + 1 # search right half
        else: # else, search value equals mid value
            return mid
    return -1 # if not returned up until this point, search value not found

even_test_list = [1, 3, 9, 11, 15, 19, 29, 35]
odd_test_list = [1, 3, 9, 11, 15, 19, 35]
test_val_smallest = 1
test_val_largest = 35

# TESTING + WORST CASE ANALYSIS/PROOF
print("Index found: " + str(binary_search_iterative(even_test_list, test_val_smallest)))
print("Searching for lowest element in even list takes: " + str(passes_iterative)) # 3 steps
passes_iterative = 0 # reset counter

print("Index found: " + str(binary_search_iterative(even_test_list, test_val_largest)))
print("Searching for largest element in even list takes: " + str(passes_iterative)) # 4 steps
passes_iterative = 0 # reset counter

print("Index found: " + str(binary_search_recursive(odd_test_list, test_val_smallest, 
                                                    0, len(odd_test_list) - 1)))
print("Searching for lowest element in even list takes: " + str(passes_recursive)) # 3 steps
passes_recursive = 0 # reset counter

print("Index found: " + str(binary_search_recursive(odd_test_list, test_val_largest, 
                                                    0, len(odd_test_list) - 1)))
print("Searching for lowest element in even list takes: " + str(passes_recursive)) # 3 steps
passes_recursive = 0 # reset counter

print()
# -----------------------------------------------------------------------------------------------------

"""
RECURSION

-> When used appropraitely, recursion will make life easier. A lot of other times, however,
   it will increase runtime complexity unnecessarily making your solution inefficient.
"""

# RECURSION IMPLEMENTATION 
# Time Complexity: O(2^N), Space Complexity: O(1)
def get_fib(position):
    if position <= 0:
        return 0
    elif position == 1:
        return 1       
    return get_fib(position - 1) + get_fib(position - 2)

"""
-> The above solution computes the values of some inputs more than once. 
   For example get_fib(4) calls get_fib(3) and get_fib(2), get_fib(3) calls get_fib(2) 
   and get_fib(1) etc. The number of recursive calls grows exponentially with n. 
   Specifically; f(1) is 2^1 steps, f(2) is 2^2 steps, f(3) is 2^3 steps, and f(4) is 2^4 steps. 
   This yields 2^1 + 2^2 + 2^3 + 2^4 + ... 2^n runtime complexity which equals O(2^(n+1)) ~ O(2^n). 
   In other words, this is a terrible algorithm.

-> In practice, if we were to use recursion to solve this problem, we should probably use a 
   hash table to store and fetch previously calculated results. 
   This will increase the space needed (space complexity) but will 
   drastically improve the runtime efficiency. This method is called memoization.
   
-> Memoization is sometimes called top-down dynamic programming.
"""
    
# RECURSION IMPLEMENTATION WITH MEMOIZATION (TOP-DOWN DYNAMIC PROGRAMMING)
# Time Complexity: O(N), Space Complexity: O(N)
def all_fib(position):
    memo = [0] * (position) # initialize hash table with all 0's
    for i in range(position): # call helper method for each value at indexes up to position
        print("index " + str(i) + " : " + str(get_fib_memo(i, memo)))
        
def get_fib_memo(position, memo):
    if position <= 0: # base case 1: return 0 if position is smaller or equal to 0
        return 0
    elif position == 1: # base case 2: return 1 if position is 1
        return 1
    elif memo[position] > 0: # if previously calculated the value at position,
        return memo[position] # return the stored value from hash table
    
    # else, we are computing value at position for the first time, store the value in hash table
    memo[position] = get_fib_memo(position-1, memo) + get_fib_memo(position-2, memo) 
    return memo[position] # return the stored value
 
# TESTING
all_fib(7) # 0, 1, 1, 2, 3, 5, 8
print()

# RECURSION IMPLEMENTATION WITH BOTTOM-UP DYNAMIC PROGRAMMING
# Time Complexity: O(N), Space Complexity: O(N)
# Bottom-up is very similar to the above top-down, but in reverse.
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

"""
-> Looking above, we can see that we only use memo[i] for memo[i - 1] and memo[i - 2]
   and we don't really need it after that. We can thus get rid of the memo "cache" and 
   just use variables!
"""

def fib_without_cache_bottom_up(position):
    if position == 0: # base case: return 0 if position is 0
        return 0
    a = 0 # represents memo[position-2], initialy the first element 0
    b = 1 # represents memo[position-1], initially the second element 1
    c = 0 # represents memo[position], initially set to 0 since unknown
    for i in range(2, position):
        c = a + b
        a = b # set a to b
        b = c # set b to c (a + b), this way we will always store the total sum at c
    
    return a + b # to understand why we return a + b, give some values and test CAREFULLY
    
"""
-> fib(0) -> return 0, fib(1) -> return 1, fib(2) -> [fib(1) -> return 1] [fib(0) -> return 0] 
   [store (0+1) at memo[2]], ...

-> Look above. Since a constant amount of work is done N times with the above fibonacci method with 
   memoization, the runtime complexity is O(n) which is a huge improvement from the previous 
   exponential runtime.
"""
# -----------------------------------------------------------------------------------------------------

"""
NOTE ABOUT PYTHON DICTIONARIES

-> In Python, the dictionary('dict') data types represent the implementation of hash tables. 

-> The keys of a Python dictionary satisfy the following requirements:
   1) The keys of the dictionary are hashable, i.e. they are generated by the hashing 
   function which generates an unique result for each unique value supplied to the hash function.  
   2) The order of data elements in a dictionary is not fixed. 
    
-> NOTE FOR ME: Check folder, 'hash table web archive', for details.
"""
# -----------------------------------------------------------------------------------------------------

"""
BUBBLE SORT
"""

# BUBBLE SORT IMPLEMENTATION
# Time Complexity: O(N^2), Space Complexity: O(1)
def bubbleSort(alist):
    # start at the end, continue to the beginning until array is sorted
    for passnum in range(len(alist)-1, 0, -1): 
        # until it hits the limit (passnum), continue checking and swapping elements one by one
        for i in range(passnum): 
            if alist[i] > alist[i+1]: # if left > right, swap
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print("Bubble sorted list: " + str(alist))

# SHORT/OPTIMIZED BUBBLE SORT IMPLEMENTATION
# Time Complexity: O(N^2), Space Complexity: O(1)
# Exits when the array is already sorted, thanks to 'exchanges' flag.
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

# TESTING
alist=[20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist)
print("Short Bubble sorted list: " + str(alist))

print()
# -----------------------------------------------------------------------------------------------------

"""
MERGE SORT
"""

# MERGE SORT IMPLEMENTATION
# Time Complexity: O(N*log(N), Space Complexity: O(N^2)
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
        # check if half (left, right) iterators don't exceed the length of their respective halves
        while i < len(lefthalf) and j < len(righthalf): 
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

# TESTING
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print("Merge sorted list: " + str(alist))

print()
# -----------------------------------------------------------------------------------------------------

"""
QUICKSORT

-> If we know that a list is nearly sorted, then quick sort will be an INEFFICIENT approach.

-> https://visualgo.net/en/sorting?slide=1 is a good website to go to visualize sorting algorithms.
"""

# QUICK SORT IMPLEMENTATION
# Time Complexity: O(N*log(N)) on average - O(N^2) on worst case, Space Complexity: O(log(N))
def quickSort(arr):
   quickSortHelper(arr, 0, len(arr) - 1) # start with low = left = 0, high = right = len(arr) - 1

def quickSortHelper(arr, left, right):
    # get a split_point so that you can split the array into two halves
    split_point = partition(arr, left, right) 
    if (left < split_point - 1): # sort left half
        quickSortHelper(arr, left, split_point - 1)
    if (right > split_point): #sort right half
        quickSortHelper(arr, split_point, right)

def partition(arr, left, right):
    # pick pivot point, since this partitioned pivot value is
    # not guarenteed to be median, we have O(N^2) runtime worst case
   pivot_value = arr[int((left+right)/2)] 
   
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

# TESTING
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print("Quick sorted list: " + str(alist))

print()
# -----------------------------------------------------------------------------------------------------

"""
RADIX (BUCKET) SORT

-> This algorithm only sorts NUMBERS!

-> Radix sort (often) makes use of another sorting algorithm, count sort.
"""

# RADIX (BUCKET) SORT IMPLEMENTATION (t
# Time Complexity: O(k * N) where k = the number of passes of the sorting algorithm,
# Space Complexity: O(N + k) 
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
  
# TESTING
print("Radix sorted list: " + str(radixSort([1, 4, 146, 25, 7, 53, 2211])))
print()
# -----------------------------------------------------------------------------------------------------

"""
HEAP SORT

-> At each step, heap sort algorithm heapifies subtree rooted at index i in a n-sized heap.
"""

# HEAP SORT IMPLEMENTATION
# Time Complexity: O(N log(N)), Space Complexity: O(1)
def heapify(arr, n, i): # heapification is done bottom-up
    largest = i # initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # see if left child of root exists and is greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # see if right child of root exists and is greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # change root, if needed 
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i] # swap 
  
        # heapify the root
        heapify(arr, n, largest) 
  
# main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # build a maxheap
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # one by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
  
# TESTING
arr = [12, 11, 13, 5, 6, 7] 
heapSort(arr) 
print("Heap sorted list: " + str(arr))
print()