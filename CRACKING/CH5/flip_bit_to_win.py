# def flip_bit_to_win(num):
    # sequences = []
    # max_length = 0
    # flipped = False
    # for i in range(32):
        # if num >> i & 1 == 1:
            # max_length += 1
        # elif not flipped:
            # max_length += 1
            # flipped = True
        # elif flipped:
        # else:
            # sequences.append(max_length)
            # flipped = False # reinstantiate the variables and prepare for a new sequence
            # max_length = 0
    
    # print(sequences)
    # return max(sequences) # the runtime of max is O(n) since it must check every element.

# There is no logical shift in Python so we implement it ourselves.
def right_logical_shift(val, n):
    if val >= 0:
        return val >> n
    else:
        return (val + 0x100000000) >> n
    
def flip_bit_to_win(num):
    # If all 1s, this is already the longest sequence.
    if ~num == 0:
        return 32
    
    # we don't need to hang on to the length of each sequence the entire time. 
    # we only need it long enough to compare each 1s sequence to immediately preceding 1s sequence
    
    current_len = 0
    previous_len = 0
    max_len = 1 # we can always have a sequence of at least one 1
    while num != 0:
        if (num & 1) == 1: # current bit is a 1
            current_len += 1
        elif (num & 1) == 0: # current bit is a 0
            # update to previous length to 0 if next bit is 0 or to current length if next bit is 1
            if ((num >> 1) & 1) == 1: # if next bit is 1
                previous_len = current_len
            else: # if next bit is 0 (00 -> len is 0)
                previous_len = 0
            current_len = 0
        
        max_len = max(previous_len + current_len + 1, max_len) # dont forget the plus 1, comes from the flipping!
        num = right_logical_shift(num, 1) # logical shift to place 0 in MSB each time
    return max_len

# (num >> 1) & 1 == num & 2 -> didn't work in Python!
       
print(flip_bit_to_win(1775))