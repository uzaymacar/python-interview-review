# O(N)
# Always write out test cases in paper

# The find() method returns the index of first occurrence of the substring (if found). 
# If not found, it returns -1.

# Here is the summary for in:
# list - Average: O(n)
# set/dict - Average: O(1), Worst: O(n)
# The O(n) worst case for sets and dicts is very uncommon, 
# but it can happen if __hash__ is implemented poorly. 
# This only happens if everything in your set has the same hash value.

def is_substring(str1, str2):
    #return str1.find(str2) != -1
    return str2 in str1

def is_rotation_smarter(str1, str2):
    if len(str1) != len(str2):
        return False
    
    return is_substring(str1 + str1, str2)  # this is the smart way  

def is_rotation(str1, str2):
    # base cases
    if len(str1) != len(str2):
        return False
    
    change = 0
    for i in range(len(str1)):
        if str1[0] not in str2:
            return False
        str1 = str1[1:] + str1[0]
        change += 1
 
        if str1[0:len(str1)-change] in str2:
            return True
            
test1 = "waterbottle"
test2 = "bottlewater"
test3 = "aterbottlew"

print(is_rotation_smarter(test2, test3))