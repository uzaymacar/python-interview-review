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
    
#testArray = [1, 2, 3, 4, 5, 6, 7]
#print(tree_helper(testArray))

def get_depth(binary_tree):
    root = binary_tree.root
    depth = 0
    while root.left != None:
        root = root.left
        depth += 1
    return depth
   
tree = Tree(TreeNode(4))

tree.root.left = TreeNode(2)
tree.root.left.left = TreeNode(1)
tree.root.left.right = TreeNode(3)

tree.root.right = TreeNode(6)
tree.root.right.right = TreeNode(7)
tree.root.right.left = TreeNode(5)

def check_balanced(root):
    print(root.value)
    original = root
    left_height = 0
    right_height = 0
    
    while root.left != None:
        root = root.left
        left_height += 1
    
    root = original
    while root.right != None:
        root = root.right
        right_height +=1
    
    if left_height != right_height:
        return False
    
    root = original
    if root.left != None:
        if not check_balanced(root.left): # do it this way! (RECURSIVE IS TRICKY!)
            return False
    if root.right != None:
        if not check_balanced(root.right):
            return False
    
    return True
    
print(check_balanced(tree.root))