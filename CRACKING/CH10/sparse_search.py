def binary_search_recursive(input_array, value, low, high, mode):
    if (low > high): #error
        return -1    
    mid = (low + high)//2
    while input_array[mid] == "":
        if mode == "right":
            mid += 1
        else:
            mid -= 1
    
    if value > input_array[mid]:
        return binary_search_recursive(input_array, value, mid + 1, high, "right") # don't forget the return statements with recursives in Python.
    elif value < input_array[mid]:
        return binary_search_recursive(input_array, value, low, mid - 1, "left")
    else:
        return mid
    
array = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
#array_test = ["at", "ball", "car", "dad"]
value = "dad"
#print(binary_search_recursive(array_test, value, 0, len(array_test) - 1))

print(binary_search_recursive(array, value, 0, len(array) - 1, "neutral"))

# print("at" < "ball") # correct way to compare strings (alphabetically) in Python
print("" < "ball")