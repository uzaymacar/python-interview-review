# To see the solution of this problem, try test cases! (the answer is always out there!)
def sorted_matrix_search(arr, x): # O(M * log(N))
    row = 0
    col = len(arr[0]) - 1
    while (row < len(arr) and col >= 0):
        if arr[row][col] == x:
            return row, col
        elif arr[row][col] > x:
            col -= 1
        else:
            row += 1
    return -1, -1
    
    
    
print(sorted_matrix_search(([0, 1, 3],
                           [2, 3, 4],
                           [5, 6, 7],
                           [7, 8, 9]), 4))