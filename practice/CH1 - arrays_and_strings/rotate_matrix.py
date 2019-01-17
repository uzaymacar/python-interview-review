# O(N^2)
# Check out from Git repo how to accomplish this in place
# char is 1 byte (8 bits)

def rotate_matrix_90(img_arr): 
    new_array = []
    new_row = []
    for c in range(len(img_arr[1])):
        for r in range(len(img_arr[0])):
            new_row.append(img_arr[r][c])
        new_array.append(new_row[::-1]) # reverse the column and make it a row
        new_row = []
    
    return new_array
    

test_array = [[1, 2, 3, 16], 
              [4, 5, 6, 15], 
              [7, 1, 0, 14],
              [10, 11, 12, 13]]


for row in rotate_matrix_90(test_array):
    print(row)
    #print('\n') no need to do this as for each loop prints in new line every time