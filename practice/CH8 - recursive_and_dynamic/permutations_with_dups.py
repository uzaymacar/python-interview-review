def permutation_helper(text):
    return get_permutations(text, len(text) - 1)

def get_permutations(text, n):
    subsets = []
    subset_maps = [0] * (256) * (1000)
    if n == 0:
        subsets.append(text[0])            
        return subsets

    item = text[n]
    prev_subsets = get_permutations(text, n - 1)
    for substr in prev_subsets:
        print(substr, item)
        for i in range(len(substr) + 1):
            new_item = ""
            if i == 0:
                new_item = item + substr
            elif i == len(substr):
                new_item = substr + item
            else:
                new_item = substr[:i] + item + substr[i:]
            hash_val = 0
            for i in range(len(new_item)):
                hash_val += ord(new_item[i]) * (10**i)
            if subset_maps[hash_val] == 0: # lookups in hashmap are O(1)
                subsets.append(new_item)
                subset_maps[hash_val] += 1
            # if new_item not in subsets: # in is O(N), you can minimize with hash maps
                # subsets.append(new_item)
    return subsets

print(permutation_helper("bbc"))