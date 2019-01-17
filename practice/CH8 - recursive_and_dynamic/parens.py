# DIDN'T WORK!

def add_paren(arr, left_rem, right_rem, text, index):
    if left_rem < 0 or right_rem < left_rem: # invalid state
        return None 
    
    if left_rem == 0 and right_rem == 0: # out of left and right parentheses
        print(arr)
        arr.append(text)
        return arr
    else:
        text_copy = ""
        # text_[index] = '(' # add left and recurse -> TypeError: 'str' object does not support item assignment
        counter1 = 0
        for char in text:
            if counter1 == index:
                text_copy += '('
            else:
                text_copy += char
        return add_paren(arr, left_rem - 1, right_rem, text_copy, index + 1)
        
        text_copy = ""
        counter2 = 0
        for char in text:
            if counter2 == index:
                text_copy += ')'
            else:
                text_copy += char
        # text[index] = ')' # add right and recurse -> TypeError: 'str' object does not support item assignment
        return add_paren(arr, left_rem, right_rem - 1, text_copy, index + 1)

# In Python, strings are immutable, so you can't change their characters in-place.
# You can, however, do the following:
# for i in str:
    # srr += i
# The reasons this works is that it's a shortcut for:
# for i in str:
    # srr = srr + i
# The above creates a new string with each iteration, 
# and stores the reference to that new string in srr.

def generate_parens(n):
    text = "" * (n*2)
    arr = []
    arr_new = add_paren(arr, n, n, text, 0)
    return arr_new

print(generate_parens(3))