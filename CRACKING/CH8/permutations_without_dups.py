def permutation_helper(text):
    return get_permutations(text, len(text) - 1)

def get_permutations(text, n):
    subsets = []
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
            subsets.append(new_item)
    return subsets

print(permutation_helper("abc"))
    
    
    