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

# LINKED LIST IMPLEMENTATION
class Element(object): # single unit (Node) in a linked list
    def __init__(self, value): # to initialize a new element
        self.value = value
        self.next = None
    
    def get_value(self): # get value (data) of element
        return self.value
        
class LinkedList(object):
    def __init__(self, head = None): # if we initialize a new LinkedList without a head, default head to None. 
        self.head = head
    
    def append(self, new_element):
        current = self.head
        if self.head: # always check if the head exists or not
            while current.next:
                current = current.next
            current.next = new_element
        else: # if self.head doesn't exist => empty list => append new element as the head
            self.head = new_element
    
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
            
    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
    
    def insert_first(self, new_element): # added for Stack implementation below
        new_element.next = self.head
        self.head = new_element
    
    def delete_first(self): # added for Stack implementation below
        if self.head: # will still work if self.head.next does not exist.
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None

#my_list = LinkedList(Element(5))
#my_list.append(Element(4))
#print(my_list.get_position(1).get_value())

def get_depth(binary_tree):
    root = binary_tree.root
    depth = 0
    while root.left != None:
        root = root.left
        depth += 1
    return depth

ll_arr = None 
   
def list_of_depths_helper(binary_tree):
    global ll_arr
    root = binary_tree.root
    depth = get_depth(binary_tree)
    initial_list = LinkedList(Element(root.value))
    output = [0] * (depth+1)
    output[0] = initial_list
    ll_arr = output
    list_of_depths(root, 1, depth)

tree = Tree(TreeNode(4))

tree.root.left = TreeNode(2)
tree.root.left.left = TreeNode(1)
tree.root.left.right = TreeNode(3)

tree.root.right = TreeNode(6)
tree.root.right.right = TreeNode(7)
tree.root.right.left = TreeNode(5)
  
def list_of_depths(root, k, max_depth):
    global ll_arr # be careful about your return values!
    # print(root, k)
    left = root.left
    right = root.right
    if ll_arr[k] == 0:
        if left != None:
            ll_arr[k] = LinkedList(Element(left.value))
        if right != None:
            if ll_arr[k] == 0:
                ll_arr[k] = LinkedList(Element(right.value))
            else:
                ll_arr[k].append(Element(right.value))            
    else:
        if left != None:
            ll_arr[k].append(Element(left.value))
        if right != None:
            ll_arr[k].append(Element(right.value))
    
    if k < max_depth:
        list_of_depths(left, k+1, max_depth)
        list_of_depths(right, k+1, max_depth)
    else:
        return
     
list_of_depths_helper(tree)
print(ll_arr[2].head.next.next.next.next.value) 
    
    