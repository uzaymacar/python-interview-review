class TreeNode(object):
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.parent = None
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
tree.root.left.parent = TreeNode(4)

tree.root.left.left = TreeNode(1)
tree.root.left.left.parent = TreeNode(2)
tree.root.left.right = TreeNode(3)
tree.root.left.right.parent = TreeNode(2)

tree.root.right = TreeNode(6)
tree.root.right.parent = TreeNode(4)

tree.root.right.right = TreeNode(7)
tree.root.right.right.parent = TreeNode(6)
tree.root.right.left = TreeNode(5)
tree.root.right.right.parent = TreeNode(6)

def leftMostChild(node):
    if node == None:
        return None
    
    while node.left != None:
        node = node.left
    
    return node

def inorderSucc(node):
    if node == None:
        return None
    
    # Found right children -> return leftmost node of right subtree.
    if node.right != None:
        return leftMostChild(node.right) # this is HOW IN ORDER TRAVERSAL WORKS!! (get leftmost of right after root)
    else:
        q = node
        x = q.parent
        # Go up until we're on left instead of right
        while x != None and x.left != q:
            q = x
            x = x.parent
    return x

# print(tree.root.right.left.value)
print(inorderSucc(tree.root.left).value)