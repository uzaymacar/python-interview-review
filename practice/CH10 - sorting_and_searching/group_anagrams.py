# Anagram is a word, phrase, or name formed by rearranging the letters of another, 
# such as spar, formed from rasp. In other words, we could say it is a permutation!

def get_hash_map(text):
    hash_map = [0] * 256
    for char in text:
        hash_map[ord(char)] += 1
    return hash_map

def group_anagrams(arr):    
    for passnum in range(len(arr) - 1, 0, -1):
        for i in range(passnum):
            if get_hash_map(arr[i]) > get_hash_map(arr[i+1]): # don't forget to compare values as always!
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
    return arr

print(group_anagrams(["abc", "def", "bac", "fed", "bca"]))

# [1, 1, 1] > [0, 1, 1] -> Python gives comparisons between arrays according to the sum of their elements!