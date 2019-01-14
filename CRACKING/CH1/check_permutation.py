# O(N)

MAX = 256
text1_map = [0] * MAX
text2_map = [0] * MAX

def compare(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

def is_permutation(text1, text2):
    if len(text1) != len(text2):
        return False
    
    for i in range(len(text1)):
        text1_map[ord(text1[i])] += 1
        text2_map[ord(text2[i])] += 1
        
    return compare(text1_map, text2_map)

string1 = "abcdefw"
string2 = "bcdaefg"
print(is_permutation(string1, string2))

    