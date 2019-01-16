class TreeNode(object):
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
    def __str__(self): # implement default print method
        return '(L:' + str(self.left) + ')' + '(V:' + str(self.value) + ')' + '(R:' + str(self.right) + ')'
    
class Tree(object):
    def __init__(self, root = TreeNode()):
        self.root = root

def tree_helper(arr):
    return minimal_tree(arr, 0, len(arr) - 1)
       
def minimal_tree(arr, low, high):
    if low > high:
        return None
    
    mid = (high+low)//2 
    root = TreeNode(arr[mid])
    root.left = minimal_tree(arr, low, mid - 1) # binary search tactic works!
    root.right = minimal_tree(arr, mid + 1, high)
    
    return root
    
testArray = [1, 2, 3, 4, 5, 6, 7]
print(tree_helper(testArray))