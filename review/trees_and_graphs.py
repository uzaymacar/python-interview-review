# A tree is a data structure composed of connected nodes (you can reach every node from the root)
# 1) Each tree has a root node, 2) The root node has zero or more child nodes,
# 3) Each child node has zero or more child nodes, and so on, 4) The tree can't contain any cycles.

class Node(object):
    def __init__(self, name = "", children = []):
        self.name = name
        self.children = children
    
class BinaryTreeNode(object): # holds for a binary tree only (2 children)
    def __init__(self, value = "", left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
class Tree(object):
    def __init__(self, root = BinaryTreeNode()):
        self.root = root

# BASIC TREE TERMINOLOGY
# Level: Root is level 1, its descendants/children are level 2, and so on.
# Height: The leaf nodes have height 0, their parents have height 1, and so on.
# Height of a Tree = Height of the Root Node
# Depth: Number of edges to the root, moves inversely with height. Root has 0 depth, 
# its children have 1 depth, and so on.
        
# TREES VS BINARY TREES [always ask which one in interview!]
# Binary trees have nodes with up to 2 children whereas trees don't have a limitation.
# A node is called a "leaf" node if it has no children.
        
# BINARY TREE VS BINARY SEARCH TREE
# A binary search tree is a binary tree in which every node fits a specific
# ordering property: all left descendents <= n < all right descendents
# The equality on the left changes from definiton to definiton so clarify with
# the interviewer (some say binary search trees can't have duplicate values.)
        
# BE CAREFUL: The ordering property holds true for ALL OF a node's descendents, not
# just the immediate children!
        
# BALANCED VS UNBALANCED
# Perfect binary trees != Balanced trees (don't fall for this!)
# A "balanced" tree is a tree that is not "terribly imbalanced"; it is balanced enough to
# ensure O(log(N)) runtimes for insert and find, but it's not necessarily 
# as balanced as it could be.
        
# COMPLETE BINARY TREE
# A complete binary tree js a binary tree in which every level of the tree is fully filled
# with the exception of the last level. To the extent that the last level is filled,
# it is filled left to right (left should come first!)
        
# FULL BINARY TREE
# A full binary tree is a binary tree in which every node has either zero or two children.
# That is, no nodes have only one child.
        
# PERFECT BINARY TREE
# A perfect binary tree is one that is both a FULL BINARY TREE and a COMPLETE BINARY TREE.
# This requires all "leaf" nodes to be at the same level and this level will have
# the maximum number of nodes as it will be the last level.
# A perfect tree must have exactly 2^k - 1 nodes.
# Never assume that a binary tree is perfect.

# BINARY TREE TRAVERSAL
        
# 1) IN-ORDER TRAVERSAL
# In order is to visit the left branch, then the current node, and then finally the right branch
# left child -> parent -> right child, visits the nodes in ASCENDING order in a BINARY SEARCH TREE
def inOrderTraversal(node):
    if node != None:
        inOrderTraversal(node.left)
        print(node)
        inOrderTraversal(node.right)
    
# 2) PRE-ORDER TRAVERSAL
# Pre order visits the current node before its child nodes (hence "pre")
# Hence, the root is always the first node visited.
def preOrderTraversal(node):
    if node != None:    
        print(node)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)
        
# 3) POST-ORDER TRAVERSAL
# Post order traversal visits the current node after its child nodes (hence "post")
# Hence, the root is always the last node visited.
def postOrderTraversal(node):
    if node != None:    
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print(node)
        
class BinarySearchTree(object):
    def __init__(self, root): # initialize a BST (binary search tree)
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
        if current: # if current node exists, go inside
            if current.value == find_val: # return True if current node's value equal to search value
                return True
            elif current.value < find_val: # call recursion on the right subtree if current node's value smaller
                return self.search_helper(current.right, find_val)
            else: # call recursion on the left subtree if current node's value is greater
                return self.search_helper(current.left, find_val)
        return False # if there are no returns up until this point, return False since the search value is not found
       
# BINARY HEAPS (MIN-HEAPS AND MAX-HEAPS)
# Min-heaps are heaps with their elements in ASCENDING order so that the root is the MINIMUM element.
# Max-heaps are heaps with their elements in DESCENDING order so that the root is the MAXIMUM element.

# A min-heap is a COMPLETE binary tree (totally filled other than the rightmost elements on the last level)
# where each node is smaller than its children.
        
# Why array based representation for Binary Heap?
# Since a Binary Heap is a Complete Binary Tree, it can be easily represented as array and array 
# based representation is space efficient. If the parent node is stored at index I, 
# the left child can be calculated by 2 * I + 1 and right child by 2 * I + 2 
# (assuming the indexing starts at 0).
# CHECK HEAP SORT IN PYTHON_SEARCHING_AND_SORTING

# We have two key operations on a min-heap: insert and extract_min

# INSERT       
# When we insert into a min-heap, we always start by inserting the element at the bottom.
# We insert at the rightmost spot so as to maintain the complete tree property.
# Then we "fix" the tree by swapping the new element with its parent and we essentially bubble
# up the min element. This takes O(log(N)) time where N = number of nodes in the heap
        
# EXTRACT MIN ELEMENT
# The minimum element is always at the top! First, remove the minimum element and swap it with the last
# element in the heap which is the BOTTOMMOST AND RIGHTMOST element. Then we bubble down this
# element, swapping it with one of its children until the MIN-HEAP PROPERTY is restored
# THERE IS NO INHERENT ORDERING BETWEEN LEFT AND RIGHT CHILD, therefore we take the SMALLER
# ELEMENT to maintain MIN-HEAP PROPERTY. This algorithm will also take O(log(N)) runtime.

# TRIES (PREFIX TREES)
# A trie is a variant of an n-ary tree in which characters are stored at each node.
# Each path down the tree may represent a word. The * nodes, sometimes called "null nodes"
# are used to indicate complete words. To implement this, we could either use a 
# a) a special type of child such as "TerminatingTrieNode" which would inherit from TrieNode or
# b) a boolean flag "terminates" within the parent node.
        
# A node in a trie could have anywhere from 1 through ALPAHABET_SIZE + 1 children.
# Hash tables can quickly lookup whether a string is a valid word or not but they can't
# tell if a string is a prefix of any valid words whereas a TRIE can do this very quickly.
        
# A trie can check if a string is a valid prefix in O(K) time where K = length of string
# Although we often refer to hash table lookups as being O(1) time, since they have to
# check each character in the case of a string, they also take O(K) time in a word lookup.
# M -> MA -> MAN -> MANY
        
# GRAPHS
# A tree is actually a type of graph, but not all graphs are trees. A tree is a connected graph
# WITHOUT cycles. A graph is simply a colelction of nodes with edges between (some of) them.
        
# 1) Graphs can be either directed (edges with arrows indicating one-way street) or 
# undirected (edges without arrows indicating two-way stree)
# 2) The graph might consist of multiple isolated subgraphs. If there is a path between every pair of
# vertices, it is called a CONNECTED GRAPH.
# 3) The graph can also have cycles. A graph without cycles is called "ACYCLIC GRAPH".

# Two common ways to represent a graph: a) Adjaceny Lists, b) Adjacency Matrices
        
# ADJACENCY LIST
# Most common way to represent a graph. Every vertex (node) stores a list of adjacent vertices.
# In an undirected graph, an edge like (a, b) would be stored TWICE: one in a's adjacent vertices
# and one in b's adjacent vertices.
        
class Graph(object): # unlike in a tree, you can't necessarily reach all the nodes from a single node!
    def __init__(self, adjacentVertices = []):
        self.nodes = adjacentVertices # adjacency list
        
class TrieNode(object):
    def __init__(self, name = "", children = []):
        self.name = name
        self.adjacent = [] # adjacency list
        self.visited = False
        
# ADJACENCY MATRIX
# An adjacency matrix is a NxN boolean matrix where N = number of nodes. A true (or 1) value
# at matrix[i][j] indicates an edge from node i to node j.
# In an undirected graph, an adjacenyc matrix will be SYMMETRIC whereas not necessarily in a directed graph.

# Graph algorithms (like breadth-first search) are usually LESS EFFICIENT to perform with a adjacency
# matrix when compared with a adjacency list.
        
# GRAPH SEARCH

# 1) DEPTH-FIRST SEARCH (DFS)
# Start at the root and explore each branch completely before moving on to the next branch.
# GO DEEP BEFORE GOING WIDE
# DFS is preferred if we want to visit every node in the graph.
# Pre-order and other forms of tree traversal are a form of DFS (because of recursion!)
# To not risk getting stuck in an infinite loop, we have to check if each node is visited before

def search_depth_recursive(root):
    if root == None:
        return None
    print(root)
    root.visited = True # don't forget to mark visited
    for node in root.adjacent:
        if node.visited == False: # search recursively only if not visited before!
            search_depth_recursive(node)
        
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

# In the above algorithm, notice that the last added neighbor will be popped, then
# subsequently its last added child will be popped, and so on. Hence the depth-first-traversal.
            
# 2) BREADTH-FIRST SEARCH (BFS)
# Start at the root and explore each neighbor before going on to any of their children.
# GO WIDE BEFORE GOING DEEP
# BFS is preferred if we want to find the shortest path.
# DON'T ASSUME THAT BFS IS RECURSIVE. IT IS NOT. RATHER, IT USES A QUEUE! 

class Queue(object): # queue implementation using standard Python list
    def __init__(self, head = None): # initiliaze with a list containing head as its first element
        self.storage = [] # don't start with head, it will equal to None

    def enqueue(self, new_element): # append to the end of the queue
        self.storage.append(new_element)

    def peek(self): # get the top of the queue
        return self.storage[0]

    def dequeue(self): # remove the top element from the queue
        return self.storage.pop(0)
    
    def isEmpty(self):
        return self.storage == []
    

# abc = Queue() # isEmpty() test
# print(abc.isEmpty()) -> True

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
        
# BIDIRECTIONAL SEARCH
# Bidirectional search is used to find the shortest node between a source and a destination node.
# It operates by essentially running two simultaneous breadth-first searches, one from each node (source and destination).
# When the searches collide, we have found a path!

# Consider a graph where every node has at most k adjacent nodes and the shortest path from
# node s to node t has length d. 
                
# a) In traditional breadth-first search, we would search up to k nodes
# in the first "level" of the search. In the second level, we would search up to k nodes
# FOR EACH of those first k nodes, so k^2 nodes total (thus far). We would do this d times
# and therefore a total runtime of O(k^d)
                
# b) In bidirectional search, we have two searches that collide after approximately d/2 levels
# (midpoint of the path). The search from s visits approximately k^(d/2) as does search from t.
# That's approximately 2k^(d/2) nodes and therefore a total runtime of O(k^(d/2))

# TIME COMPLEXITIES OF BFS AND DFS
# The Time complexity of both BFS and DFS will be O(V + E), where V is the number of vertices, 
# and E is the number of Edges. This again depends on the data strucure that we user to represent 
# the graph. If it is an adjacency matrix, it will be O(V^2) . If we use an adjacency list, it will 
# be O(V+E). The difference is a sparsely connected graph and a densely connected graph.
# Therefore, O(V+E) means whichever term is bigger will dominate the time complexity. 
# That is why the time complexity of BFS is O(V+E).