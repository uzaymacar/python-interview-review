# O(N * M)

def zero_matrix(arr): # since you are returning the list, you can modify it inside and the modified copy will be returned
    # couldn't solve because tried to solve in place, sometimes its better to modularize
    # when doing in place, the 0's you have created will affect the next iterations!
    
    # print(len(arr), len(arr[2])) # len(arr) gives the row count, len(arr[i]) gives the column count
    to_be_zeroed_rows = []
    to_be_zeroed_columns = []
    
    for r in range(len(arr)):
        for c in range(len(arr[1])):
            if arr[r][c] == 0:
                to_be_zeroed_rows.append(r)
                to_be_zeroed_columns.append(c)
                
    for row in to_be_zeroed_rows: # do it here so these get dropped in big-O Notation
        zero_row(arr, row) 
    
    for column in to_be_zeroed_columns: # do it here so these get dropped in big-O Notation
        zero_column(arr, column)
        
    return arr          

def zero_row(arr, row): # modularize
    for i in range(len(arr[0])):
        arr[row][i] = 0
    
def zero_column(arr, column): # modularize
    for i in range(len(arr)):
        arr[i][column] = 0

test_array = [[10, 7, 4, 1],
              [11, 1, 5, 2],
              [12, 0, 6, 3],
              [13, 14, 15, 16],
              [1, 2, 3, 4]]


for row in zero_matrix(test_array):
    print(row)
    
