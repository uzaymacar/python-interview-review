# O(N)

MAX = 256
char_map = [0] * MAX

def isUnique(text):
    for character in text:
        if char_map[ord(character)] != 0:
            return False
        else:
            char_map[ord(character)] += 1
    return True

test_string = "abc2defgh2"
print(isUnique(test_string))