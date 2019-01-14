# STACKS

# Stacks are useful in certain recursion algorithms
class StackNode(object):
    def __init__(self, val = None):
        self.data = val
        self.next = None
    
    def get_value(self):
        return self.data

class Stack(object): # stack of dinner plates, LIFO!
    def __init__(self, first = None):
        self.top = first
        
    def pop(self):
        if self.top == None:
            return None
        item = self.top.value
        self.top = self.top.next
        return item
    
    def push(self, item):
        new_node = StackNode(item)
        new_node.next = self.top
        self.top = new_node
        
    def peek(self):
        if self.top == None:
            return None
        return self.top.data
    
    def isEmpty(self):
        return self.top == None

# QUEUES
        
# It is especially easy to mess up updating the first and the last nodes in a queue,
# be sure to double check this. Queues are often used in "bread-first search" or
# in implementing a "cache". In "bread-first-search", we use a queue to store a list
# of nodes that we need to process. Each time we process a node, we add its adjacent
# nodes to the back of the queue. This allows us to process nodes in the order in
# which they are viewed.

class QueueNode(object): # exactly similar to a StackNode
    def __init__(self, val = None):
        self.data = val
        self.next = None
        
    def get_value(self):
        return self.data
    
class Queue(object): # queue (line) at a ticket stand, FIFO!
    def __init__(self, frst = None, lst = None):
        self.first = frst
        self.last = lst
        
    def add(self, item):
        new_node = QueueNode(item)
        if self.last != None:
            self.last.next = new_node
        self.last = new_node
        if self.first == None:
            self.first = self.last
            
    def remove(self):
        if self.first == None:
            return None
        data = self.first.data
        self.first = self.first.next
        if self.first == None:
            self.last = None
        return data
    
    def peek(self):
        if self.first == None:
            return None
        return self.first.data
    
    def isEmpty(self):
        return self.first == None


# class ArrayStack(object):
   # def __init__(self, first_len = 0, second_len = 0, third_len = 0):
        # self.array = [] * 100
        # self.first = self.array[0: first_len] 
        # self.second = self.array[first_len: second_len]
        # self.third = self.array[second_len: third_len]
        
    # def pop2(self):
        # if self.top == None:
            # return None
        # item = self.top.value
        # self.top = self.top.next
        # return item
    
    # def push2(self, item):
        # new_node = StackNode(item)
        # new_node.next = self.top
    
    
# def get_stack():
    # stack1counter = 0
    # stack2counter = 0
    # stack3counter = 0
    # three_stacks_array = []

## DESIGN THREE IN ONE (3 stacks in one array)