"""
TREE

-> A tree is a data structure composed of connected nodes. Connected means 
   that every node is reachable from the root, one way or another.
   
-> There are 4 basic rules to follow:
   1) Each tree has a root node.
   2) The root node has zero or more child nodes.
   3) Each child node has zero or more child nodes, and so on.
   4) The tree doesn't contain any CYCLES.

-> Binary trees and binary tree nodes are the most frequently implemented
   structures for interviews.
"""

# BASIC TREE NODE IMPLEMENTATION
class Node(object):
    def __init__(self, value = "", adjacent = []):
        self.value = value
        self.adjacent = adjacent
        self.visited = False
    
    def __str__(self):
        return "{Value: " + str(self.value) + ", Children: [" + str([str(node) for node in self.adjacent]) + "]}"

# BINARY TREE NODE IMPLEMENATION 
# A binary tree node has a maximum of 2 children, denoted as left and right.
class BinaryTreeNode(object): # inheritance from node
    def __init__(self, value = "", left = None, right = None): # constructor for a binary tree node
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return "{Value: " + str(self.value) + ", [L: " + str(self.left) + ", R: " + str(self.right)  + "]}"

# BASIC TREE IMPLEMENTATION
class Tree(object):
    def __init__(self, root = BinaryTreeNode()): # constructor for a tree
        self.root = root # root defualtly initiliazes to a binary tree node
    
    def __str__(self):
        if self.root == None: # base case
            return "Empty Tree"
        
        return str(self.root) 

"""
-> NOTICE: We simply return self.root cast to str because we have already defined __str__()
   for BinaryTreeNode class to be a recursive one; it prints out the whole tree given only the root.
   
-> This approach is definitely not the prettiest one. A better solution would be to just
   to return the value of the BinaryTree node instance inside the __str()__ function.
"""
  
# TESTING
binary_tree = Tree(BinaryTreeNode("A", BinaryTreeNode("B", BinaryTreeNode("C", BinaryTreeNode("D"))), 
                                  BinaryTreeNode("E")))
print("Printing binary tree: " + str(binary_tree))

print()         
# -----------------------------------------------------------------------------------------------------

"""
BASIC TREE TERMINOLOGY

-> Level: Root is level 1, its descendants/children are level 2, and so on.
-> Height: The leaf nodes have height 0, their parents have height 1, and so on.
-> Height of a Tree = Height of the Root Node
-> Depth: Number of edges to the root, moves inversely with height. Root has 0 depth, 
   its children have 1 depth, and so on.
"""
  
def get_depth(binary_tree):
    return get_depth_helper(binary_tree.root)

def get_depth_helper(node): # recursive method 
    current_depth = -1 # not counted for root yet, start with -1
    
    for child_node in node.adjacent:
        current_depth = max(current_depth, get_depth_helper(child_node)) # recursively set depth
    
    return current_depth + 1 # plus one comes from the newly counted node

binary_tree_depth2 = Tree(Node("A", [Node("B", [Node("D")]), Node("C")]))
assert(get_depth(binary_tree_depth2) == 2)

binary_tree_depth1 = Tree(Node("A", [Node("B")]))
assert(get_depth(binary_tree_depth1) == 1)

binary_tree_depth0 = Tree(Node("A"))
assert(get_depth(binary_tree_depth0) == 0)

# -----------------------------------------------------------------------------------------------------

"""
ADVANCED TREE TERMINOLOGY

-> In an interview, you ideally want to clarify the category of the tree structure you are expected
   to implement or work on. This is not only for clarity, but also for checking the correct
   base and edge cases.

TREES VS BINARY TREES 
-> Binary trees have nodes with up to 2 children whereas trees don't have a limitation.
   
-> Side Note: A node is called a "leaf" node if it has no children.
        
BINARY TREE VS BINARY SEARCH TREE
-> A binary search tree is a special type of binary tree in which every node fits a specific
   ordering property: all left descendents <= n < all right descendents.
-> The equality on the left changes from definiton to definiton so clarify with
   the interviewer; some say binary search trees can't have duplicate values.
        
-> BE CAREFUL: The ordering property holds true for ALL OF a node's descendents, not
   just the immediate children!
        
BALANCED VS UNBALANCED BINARY TREE
-> Perfect binary trees != Balanced binary trees (don't fall for this!)
-> A "balanced" tree is a tree that is not "terribly imbalanced"; it is balanced enough to
   ensure O(log(N)) runtimes for insert and find, but it's not necessarily as balanced as it could be.
        
COMPLETE BINARY TREE
-> A complete binary tree is a binary tree in which every level of the tree is fully filled
   with the exception of the last level. 
-> To the extent that the last level is filled, it is filled left to right, meaning that left children 
   should be filled before right children.
"""

# COMPLETENESS IMPLEMENTATION
def check_completeness(binary_tree):
    queue = [] # queue (FIFO) for breadth first (level) traversal
    full_node = True # assume we start with a full node, will update this flag accordingly
    root = binary_tree.root # extract root
    
    if root == None: # base case: empty tree = complete
        return True
    
    queue.append(root) # initialize queue with root
    while queue: # loop until no element is left inside the queue
        node = queue.pop(0) # dequeue 'first in' node
        
        if node.left: # check if left child is present first (left-to-right fill)
            if full_node == False: # if we have seen a non-full node before visiting the left child,
                return False # we have a space BEFORE the last level, hence not complete
            queue.append(node.left) # enqueue left child
        else: # if this is a node with no left child, set flag to False
            full_node = False
        
        if node.right: # check if right child is present second (left-to-right fill)
            if full_node == False: # if seen a non-full node before visiting the right child, because
                return False # a) left child or b) a space in a level above, hence not complete
            queue.append(node.right) # enqueue left child
        else: # if this is a node with no right child, set flag to False
            full_node = False
            
    return True # if this line is reached, the tree has to be complete

# TESTING   
complete_binary_tree = Tree(BinaryTreeNode("A", left = BinaryTreeNode("B", 
                            left = BinaryTreeNode("D")), right = BinaryTreeNode("C")))
assert(check_completeness(complete_binary_tree) == True)

uncomplete_binary_tree = Tree(BinaryTreeNode("A", left = BinaryTreeNode("B", 
                              left = BinaryTreeNode("D")), right = BinaryTreeNode("C", 
                                     left = BinaryTreeNode("E"))))
assert(check_completeness(uncomplete_binary_tree) == False)

"""    
FULL BINARY TREE
-> A full binary tree is a binary tree in which every node has either zero or two children.
-> Equivalently, this means that no nodes have only one child.
"""

# FULLNESS IMPLEMENTATION
def check_fullness(binary_tree):
    return check_fullness_helper(binary_tree.root)

def check_fullness_helper(node):
    if node != None: # remember to check for the null case
        child_count = 0 # child count
        if node.left != None:
            child_count += 1
        if node.right != None:
            child_count += 1  
        if child_count != 0 and child_count != 2: # if child count is 1, return False
            return False
        # two recursive calls combined
        return check_fullness_helper(node.left) and check_fullness_helper(node.right) 
    return True # return True in the null case -> it doesn't break any rules

# TESTING
full_binary_tree = Tree(BinaryTreeNode("A", left = BinaryTreeNode("B"), right = BinaryTreeNode("C")))
assert(check_fullness(full_binary_tree) == True)

unfull_binary_tree = Tree(BinaryTreeNode("A", left = BinaryTreeNode("B", left = BinaryTreeNode("D")), 
                          right = BinaryTreeNode("C")))
assert(check_fullness(unfull_binary_tree) == False)

"""
PERFECT BINARY TREE
-> A perfect binary tree is one that is both a FULL BINARY TREE and a COMPLETE BINARY TREE.

-> This requires all "leaf" nodes to be at the same level and this level will have
   the maximum number of nodes as it will be the last level.

-> A perfect tree must have exactly 2^k - 1 nodes.

-> Never assume that a binary tree is perfect.
"""

# PERFECTNESS IMPLEMENTATION
def check_perfectness(binary_tree):
    return check_fullness(binary_tree) and check_completeness(binary_tree)

# TESTING
perfect_binary_tree = Tree(BinaryTreeNode("A", left = BinaryTreeNode("B"), 
                           right = BinaryTreeNode("C")))
assert(check_perfectness(perfect_binary_tree) == True)

unperfect_binary_tree = Tree(BinaryTreeNode("A", left = BinaryTreeNode("B", 
                             left = BinaryTreeNode("D")), right = BinaryTreeNode("C")))
assert(check_fullness(unperfect_binary_tree) == False)

# -----------------------------------------------------------------------------------------------------

"""
BINARY TREE TRAVERSAL

-> Conventionally, there exists 3 ways to traversa binary tree:
   1) In-order traversal
   2) Pre-order traversal
   3) Post-order traversal
    
-> All 3 binary tree traversal methods noted above are examples of DFS (depth-first-search).
"""
        
"""
-> In-order traversal visits the left branch, then the current node, and then finally the right branch.
-> left child -> parent -> right child, visits the nodes in ASCENDING order in a BINARY SEARCH TREE,
   hence the name in-order.
"""

# IN-ORDER TRAVERSAL IMPLEMENTATION
def inOrderTraversal(node):
    if node != None:
        inOrderTraversal(node.left)
        print(node)
        inOrderTraversal(node.right)

"""
-> Pre-order traversal visits the current node before its child nodes (hence "pre")
-> Hence, the root is always the first node visited.
"""

# PRE-ORDER TRAVERSAL IMPLEMENTATION
def preOrderTraversal(node):
    if node != None:    
        print(node)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

"""
-> Post-order traversal visits the current node after its child nodes, hence the name post.
-> The root is always the last node visited.
"""

# POST-ORDER TRAVERSAL IMPLEMENATION
def postOrderTraversal(node):
    if node != None:    
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print(node)

# -----------------------------------------------------------------------------------------------------

"""
BINARY SEARCH TREE

-> Time Complexities:
   Access -> O(log(N)) on average - O(N) on worst case
   Search -> O(log(N)) on average - O(N) on worst case
   Insertion -> O(log(N)) on average - O(N) on worst case
   Deletion -> O(log(N)) on average - O(N) on worst case
   
-> Thus, O(log(N)) on average - O(N) on worst case runtime complexity holds for access, search,
   insertion, and deletion in a binary search tree.
   
-> Space Complexity: O(N)
"""

# BINARY SEARCH TREE IMPLEMENTATION
class BinarySearchTree(object):
    def __init__(self, root): # constructor for a BST (binary search tree)
        self.root = BinaryTreeNode(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val) # initialize recursive method

    def insert_helper(self, current, new_val): # remember to use helpers in recursive questions
        if current.value < new_val: # if current value is smaller than new value, check right
            if current.right: # if right element exists, compare with it by calling recursion
                self.insert_helper(current.right, new_val)
            else: # if right element doesn't exits, simply place the value inside a node here
                current.right = BinaryTreeNode(new_val)
        else: # if current value is larger (or equal to) than the new value, check left
            if current.left: # if left element exists, compare with it by calling recursion
                self.insert_helper(current.left, new_val)
            else: # if left element doesn't exist, simply place the value inside a node here
                current.left = BinaryTreeNode(new_val)

    def search(self, find_val): 
        return self.search_helper(self.root, find_val) # initialize recursive methods

    def search_helper(self, current, find_val):
        if current: # iff current node exists, go inside
            if current.value == find_val: # return True if node's value equal to search value
                return True
            # call recursion on the right subtree if node's value smaller than search value
            elif current.value < find_val: 
                return self.search_helper(current.right, find_val)
            # call recursion on the left subtree if current node's value greater than search value
            else: 
                return self.search_helper(current.left, find_val)
        # if there are no returns up until this point, return False since the search value is not found
        return False 

# -----------------------------------------------------------------------------------------------------

"""
BINARY HEAPS (MIN-HEAPS AND MAX-HEAPS)

-> Min-heaps are heaps with their elements in ASCENDING order so that the root is the MINIMUM element.
-> Max-heaps are heaps with their elements in DESCENDING order so that the root is the MAXIMUM element.

-> A min-heap is a COMPLETE (totally filled other than the rightmost elements on the last level) 
   binary tree where each node is smaller than its children.
        
-> Why should you choose array based representation for binary heap?
   Since a Binary Heap is a complete binary tree, it can be easily represented as array,
   and array based representation is space efficient. 
   
-> If the parent node is stored at index I:
   a) the left child index can be calculated by [2 * I] + 1, and
   b) the right child index can be calculated by [2 * I] + 2,
   assuming that indexing starts at 0.
    
-> NOTE FOR ME: Check heap sort in python_searching_and_sorting

-> By convention and as an industry practice, most algorithms implement min-heap 
   rather than the max-heap.
    
-> We have two key operations on a min-heap: 1) insert, and 2) extract minimum element

-> INSERT       
   a) When we insert an element into a min-heap, we always start by inserting the element at 
   the bottom. We insert at the rightmost spot so as to maintain the complete tree property.
   b) Then we "fix" the tree by swapping the new element with its parent (if smaller than the parent)
   and we essentially bubble up the min element. 

-> Insert operation takes O(log(N)) time where N = number of nodes in the heap.
        
-> EXTRACT MINIMUM ELEMENT
   The minimum element is always at the top! 
   a) First, remove the minimum element and swap it with the last element in the heap which is the 
   BOTTOMMOST AND RIGHTMOST element. 
   b) Then we bubble down this element, swapping it with one of its children until the MIN-HEAP 
   PROPERTY (parents always hold values smaller than children) restored.

-> Extracting minimum element operation also takes O(log(N)) runtime where N = number of nodes in the 
   heap.
   
-> IMPORTANT: There is no inherent ordering between the left and the right child. Therefore, we take 
   the SMALLER ELEMENT to maintain MIN-HEAP PROPERTY.
"""

# TODO: Implement Insert operation below!

# MIN-HEAP IMPLEMENTATION FROM BINARY TREE NODE
class MinHeap_RAW(object): # class for binary search tree
    def __init__(self, root = BinaryTreeNode()): # constructor for a min-heap
        self.root = root
        
    def extract_min(self):
        print("Extracting: " + str(self.root.value))
        
        # find the rightmost element
        node = self.root # start with root node
        parent = None # represents the node iterator's parent
        while node.right: # while node has a right child
            parent = node # store node before updated as the parent
            node = node.right # update node with its right child
        
        self.root.value = node.value # swap root value with the bottom-rightmost value
        parent.right = None # delete the bottom-rightmost node
        print(self.root)
        # restore min-heap property
        node = self.root # reset node iterator, starts with root node 
        _ = float('inf') # represents the value of a non-existing (None) node
        # loop to bubble down node as you find smaller children
        while node.value > min(node.left.value if node.left else _, 
                               node.right.value if node.right else _):
    
            tmp = node.value # hold node's value at temp
            # if left child has a smaller value than the right child, swap left with node
            if node.left.value if node.left else _ < node.right.value if node.right else _:
                print("Swapping " + str(node.left.value) + " with " + str(node.value))
                node.value = node.left.value # update node's value to the left child's value
                node.left.value = tmp # update left child's value to previously stored node's value
                node = node.left # update node iterator as the left child
            # if right child has a smaller value than the left child, swap right with node
            elif node.right.value if node.right else _ < node.left.value if node.left else _:
                print("Swapping " + str(node.right.value) + " with " + str(node.value))
                node.value = node.right.value # update node's value to the right child's value
                node.right.value = tmp # update right child's value to previously stored node's value
                node = node.right # update note iterator as the left child
            # else, both left and right child are non-existing (_), and break
            else: 
                break
        print("Finished extraction")
     
    def __str__(self):
        if self.root == None: # Base case
            return "Empty Min-Heap" 
        
        return str(self.root)
         
# TESTING       
min_heap = MinHeap_RAW(BinaryTreeNode(1, BinaryTreeNode(2, 
                              BinaryTreeNode(3, BinaryTreeNode(4))), BinaryTreeNode(5)))

print("Printing min-heap: " + str(min_heap))
print()

min_heap.extract_min()
print()
print("Extracted min-heap: " + str(min_heap))
print()

"""
-> As can be seen from above, implementing a min-heap like a binary tree through the binary tree class
   is very much tedious. This is why we prefer an array-based implementation for min-heap.

-> We have built-in functions in Python to take care of the min-heap property for insertions and 
   extractions. These functions come from the 'heapq' Python module.
   
-> from heapq import heappush, heappop, heapify
   heappop - pops and returns the smallest element of the heap 
   heappush - pushes the node with given value onto the heap, maintaining the min-heap property 
   heapify - transforms (in place) list into heap in linear time [O(N)]
   
-> For the sake of practice, it is beneficial to try to implement min-heap by our own, without the
   aid of built-in functions.
"""

# MIN-HEAP IMPLEMENTATION FROM ARRAY
# TODO: Finish min-heap implementation from array.
# class MinHeap_ARR(object):
# -----------------------------------------------------------------------------------------------------

"""
TRIES (PREFIX TREES)

-> A trie is a special variant of an n-ary tree in which characters are stored at each node.

-> Each path down the tree may represent a word. 

-> The * nodes, sometimes called the "null nodes", are used to indicate complete words. 
   To implement this, we could either use a:
   a) a special type of child such as "TerminatingTrieNode" which would inherit from TrieNode or 
   b) a boolean flag "terminates" within the parent node.
        
-> A node in a trie could have anywhere from 1 through ALPAHABET_SIZE + 1 children.

-> Hash tables can quickly lookup whether a string is a valid word or not but they can't
   tell if a string is a prefix of any valid words whereas a TRIE can do this very quickly.
        
-> A trie can check if a string is a valid prefix in O(K) time where K = length of the string.

-> Slight Trick: Although we often refer to hash table lookups as being O(1) time, since they have to
   check each character in the case of a string, they also take O(K) time in a word lookup.

-> Example of a simple trie: M -> MA -> MAN -> MANY
"""

# TRIE NODE IMPLEMENTATION
class TrieNode(object):
    def __init__(self, character = "", adjacent = [], end = False):
        self.character = character
        self.adjacent = adjacent # adjacency list
        self.visited = False
        if end: # if end of word is indicated,
            self.end_of_word() # call end_of_word() method
    
    def end_of_word(self): # method to mark/indicate complete words by null node
        if self.adjacent: # if there exist other brances (example: m-a-n -> -* and -> -y)
            self.adjacent.append("*") # append to list
        else: # if there exists no branches,
            self.adjacent = ["*"] # simply set adjacent array to null node
    
    def __str__(self):
        return self.character + str([str(next_node) for next_node in self.adjacent])

# TRIE IMPLEMENTATION
class Trie(object):
    def __init__(self, root = TrieNode("")):
        self.root = root
    
    def __str__(self):
        # we might have gone for a queue approach (breadth-first-search/level) but
        # will, again, use the recursive approach in the __str__() method of TrieNode for simplicity.
        return str(self.root)
            

# TESTING
trie = Trie(TrieNode("M", [TrieNode("A", [TrieNode("N", 
       [TrieNode("Y", end = True)], end = True)]), 
       TrieNode("Y", end = True)])) 
    
print(trie) # looks ugly in the console, should use pattern matching to read appropraitely
print()
# -----------------------------------------------------------------------------------------------------

"""
GRAPHS

-> A tree is actually a type of graph, but not all graphs are trees. 

-> A tree is a connected graph WITHOUT cycles, whereas a graph is simply a colelction of nodes 
   with edges between (some of) them.
  
-> 3 Categorizations For Graphs:      
   1) Graphs can be either directed (edges with arrows indicating one-way street) or 
   undirected (edges without arrows indicating two-way street)
   2) The graph might consist of multiple isolated subgraphs. If there is a path between every pair of
   vertices, it is called a CONNECTED GRAPH.
   3) The graph can also have cycles. A graph without cycles is called "ACYCLIC GRAPH".

-> Two common ways to implement/represent a graph: 
   a) Adjaceny Lists, b) Adjacency Matrices
    
-> IMPORTANT NOTE: Unlike in a tree, you can't necessarily reach all the nodes from a single node!
   These are called UNCONNECTED graphs.

-> There are 2 main ways to implement graphs:
   1) Adjacency Lists
   2) Adjacency Matrix

ADJACENCY LIST
-> Most common way to represent a graph. 
-> Every vertex (node) stores a list of adjacent vertices.
-> In an undirected graph, an edge like (a, b) would be stored TWICE: 
   one in a's adjacent vertices and one in b's adjacent vertices.
   
ADJACENCY MATRIX
-> An adjacency matrix is a NxN boolean matrix where N = number of nodes. 
-> A true (or 1) value at matrix[i][j] indicates an edge from node i to node j.
-> In an undirected graph, an adjacenyc matrix will be SYMMETRIC 
   whereas NOT necessarily in a directed graph.

-> Graph algorithms, like breadth-first search (BFS) are usually LESS EFFICIENT 
   to perform with a 2) adjacency matrix when compared with a 1) adjacency list.

-> Takeaway: Try to use adjaceny lists for efficiency, as much as possible.

-> Idea: Chess board can also be considered a graph. However, representing the chess board
   with an adjaceny list would be ridiculous! There are places where adjacency matrixes
   are appropraite as well.
"""
# TODO: Implement vertex
#class Vertex(object):
    
class Graph(object): 
    def __init__(self, vertices = []):
        self.nodes = vertices # adjacency list
        
# TODO: implement graph with adjacency matrix     

# -----------------------------------------------------------------------------------------------------
     
"""
GRAPH SEARCH

1) DEPTH-FIRST SEARCH (DFS)
-> Start at the root and explore each branch completely before moving on to the next branch.

-> Slogan: Go Deep Before Going Wide

-> DFS is preferred if we want to visit every node in the graph.

-> Pre-order and other forms of tree traversal are a form of DFS, because of their recursive approach!

-> IMPORTANT: To not risk getting stuck in an infinite loop, we have to check if each node is 
   VISITED or NOT before!
   
-> For DFS, there exists both a recursive and an iterative implementation using stack.
"""

# RECURSIVE DFS
def search_depth_recursive(root):
    if root == None:
        return None
    print(root)
    root.visited = True # don't forget to mark visited
    for node in root.adjacent:
        if node.visited == False: # search recursively only if not visited before!
            search_depth_recursive(node)

# ITERATIVE DFS        
def search_depth_iterative(root):
    stack = [root] # stack initialized with the root node
    # visited = [] # visited list will hold the nodes in place as they are visited/print
    # Instead of a 'visited' list, we will make use of the node object property 'visited'.
    
    while stack: # while there are element in stack
        node = stack.pop() # pop the 'last in' element 
        if node.visited == False: # if the popped element is not visited,
            print(node) # visit the node
            node.visited = True # don't forget to mark visited
            for neighbor in node.adjacent: # add all neighbours to the stack
                stack.append(neighbor) 

"""
-> In the above algorithm, notice that the last added neighbor will be popped, then
   subsequently its last added child will be popped, and so on. Hence, a depth-first-traversal.
"""
            
"""
2) BREADTH-FIRST SEARCH (BFS)
-> Start at the root and explore each neighbor before going on to any of their children.

-> Slogan: Go Wide Before Going Deep

-> BFS is preferred if we want to find the shortest path.

-> For BFS, there exists a single iterative implementation using queue.

-> Important Note: Remember, we can always use a Python array/list for implementing 
   BOTH stack and queue.
"""

# TODO: Check if above statement is correct

# QUEUE IMPLEMENTATION (imported from lists.py for convenience)
from lists import Queue

# ITERATIVE BFS
def search_breadth(root):
    queue = Queue()
    root.visited = True
    queue.enqueu(root) # add to the end of the queue.
    
    while not queue.isEmpty(): # while queue is not empty, continue visiting nodes!
        r = queue.dequeue() # remove from the front of the queue
        print(r)
        for node in r.adjacent:
            if node.visited == False:
                node.visited = True
                queue.enqueue(node) # append adjacents to the queue one by one


"""
TIME COMPLEXITIES OF BFS AND DFS

-> The time complexity of both BFS and DFS will be O(V + E), where V is the number of vertices, 
   and E is the number of Edges. This, again, depends on the data strucure that we use to represent 
   the graph. 
   
-> If it is an adjacency matrix, it will be O(V^2). 
   If we use an adjacency list, it will be O(V+E). 
   
-> The difference in time complexities seen above, is a sparsely connected graph and a densely 
   connected graph.

-> O(V+E) complexity means whichever term is bigger will dominate in the runtime. 
"""
                
# -----------------------------------------------------------------------------------------------------
     
"""
BIDIRECTIONAL SEARCH

-> Bidirectional search is used to find the shortest node between a source and a destination node.

-> It operates by essentially running two simultaneous breadth-first searches, one from each node 
   (source and destination). When the searches collide, it means we have found a path!

-> Consider a graph where every node has at most k adjacent nodes and the shortest path from
   node s to node t has length d: 
                
   a) In traditional breadth-first search, we would search up to k nodes
   in the first "level" of the search. In the second level, we would search up to k nodes
   FOR EACH of those first k nodes, so k^2 nodes total (thus far). We would do this d times
   and therefore a total runtime of O(k^d)
                
   b) In bidirectional search, we have two searches that collide after approximately d/2 levels
   (midpoint of the path). The search from s visits approximately k^(d/2) as does search from t.
   That's approximately 2k^(d/2) nodes and therefore a total runtime of O(k^(d/2))
"""
# TODO: Implement bidirectional search and do a runtime analysis!