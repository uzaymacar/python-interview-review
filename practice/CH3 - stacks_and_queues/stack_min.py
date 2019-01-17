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
        # self.min_set = set()
        self.min_element = first.data
        
    def pop(self):
        if self.top == None:
            return None
        item = self.top.data
        self.top = self.top.next
        return item
    
    def push(self, item):
        if (item < self.min_element):
            self.min_element = item
        # self.min_set.add(item)
        new_node = StackNode(item)
        new_node.next = self.top
        self.top = new_node
        
    def peek(self):
        if self.top == None:
            return None
        return self.top.data
    
    def isEmpty(self):
        return self.top == None
    
    def get_min(self):
        return self.min_element
        # print(self.min_set)
        # return list(self.min_set)[0]
               
stack = Stack(StackNode(5))
stack.push(4)
stack.push(3)
stack.push(15)
stack.push(25)

print(stack.get_min())

#for i in range(5):
    #print(stack.pop())
    
set1 = set()
set1.add(4)
set1.add(1)
set1.add(2)
set1.add(7)
#print(set1)


