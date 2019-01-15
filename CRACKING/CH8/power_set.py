def get_subset_recursive(arr, n):
    # all_subsets = [[]] -> since recursive, adding base case here would mess things up!
    all_subsets = None
    if len(arr) == n: # base case, add empty set
        all_subsets = []
        all_subsets.append([])
    else:
        all_subsets = get_subset_recursive(arr, n + 1)
        item = arr[n]
        more_subsets = []
        for subset in all_subsets: # for all of the previous subsets copy the new item and merge
            new_subset = []
            print(subset)
            for value in subset: # remember that subset is an array
                print(value)
                new_subset.append(value) # pass all values to the new subset
            # new_subset = subset -> we don't want to set equal when the array is empty
            new_subset.append(item) # finally, in addition to the previous copy subset's all items, add the current iteration item
            more_subsets.append(new_subset) # append this new subset
        
        for subset in more_subsets: # all_subsets had the previous copy subsets, add the new item copied subsets to this to get all of the subsets
           all_subsets.append(subset)
           
    return all_subsets

# When stuck in a problem like this, always think: How do I go from the nth step
# to the (n+1)th step? Here, the answer was to copy over the previous subsets
# and add the final element.
print(get_subset_recursive([1, 2, 3, 4], 0))
        
    