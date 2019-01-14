# O(N)
MAX = 256

char_mapping = [0] * MAX
# char_mapping_2 = [0] * MAX

def is_one_away(text1, text2):
    if len(text1) - 1 == len(text2):
        return is_one_edit_away(text1, text2)
    elif len(text2) - 1 == len(text1):
        return is_one_edit_away(text2, text1)
    elif len(text1) == len(text2):
        return is_one_edit_away_same_length(text1, text2)
    else:
        return False
        
def is_one_edit_away_same_length(str1, str2):
    #for i in range(len(str1)):
    replace = 0 # dont put global counters inside loop
    for i1, i2 in zip(str1, str2):     
        if i1 != i2:
            replace += 1
    
    return replace == 1 or replace == 0

def is_one_edit_away(str1, str2):
    # str1 has greater length than str2
    str1counter = 0 # iterator for str1
    str2counter = 0 # iterator for str2
    replace = 0 # replace count
    while str1counter < len(str1) and str2counter < len(str2): # loop over them both
        if str1[str1counter] != str2[str2counter]: # increment str1counter and replace if not equal
            replace += 1
            str1counter += 1
        else:
            str1counter += 1 # increment both counters if they are equal
            str2counter += 1
    
    if (str2counter >= len(str2)) and replace == 0: # if replace == 0 and str2counter has exceeded its limits,
        return True # two strings one edit away as the only differing character is the last character evident from above
    
    return replace == 1 # otherwise, one edit away if and only if replace (edit) count is 1

# def is_one_edit_away(text1, text2):
    # don't forget to check for base cases
    # edit_count = 0
    # for char in text1:
        # char_mapping[ord(char)] += 1
    
    # for char in text2:
        # char_mapping[ord(char)] -= 1
        # if char_mapping[ord(char)] >= 1:
            # edit_count += 1
        # else:
            # edit_count -= 1
        
        #char_mapping_2[ord(char)] += 1
        
    # char_mapping_1 - char_mapping_2 subtraction won't work because these are not numpy arrays
    # for subtraction to work you have to zip like below
    # result = [x - y for (x, y) in zip(char_mapping_1, char_mapping_2)]
    
    # edit = 0
    # for occurrence in char_mapping:
        # edit += abs(occurrence)
    
    # return edit == 1 or edit == 0 # read the question carefully!

text1 = "ales"
text2 = "pales"
print(is_one_away(text1, text2))
        
arr1 = [1, 3, 5, 7]
arr2 = [6, 8, 10, 12, 14]
print(set(zip(arr1, arr2))) # to see how we can get elements from two different arrays at the same time