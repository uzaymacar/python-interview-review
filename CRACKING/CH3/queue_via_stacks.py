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
        # self.min_element = first.data
        
    def pop(self):
        if self.top == None:
            return None
        item = self.top.data
        self.top = self.top.next
        return item
    
    def push(self, item):
        # if (item < self.min_element):
            # self.min_element = item
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


# QUEUE IMPLEMENTATION USING STANDARD LIST
        
class Queue(object): #FIFO
    def __init__(self, head = None, butt = None): # initiliaze with a list containing head as its first element
        self.top = Stack()
        self.bottom = Stack()
        # self.bottom = Stack(StackNode(butt)) if you do it like this isEmpty will return False! Be careful!

    def enqueue(self, new_element): # append to the end of the queue
        if self.bottom.isEmpty():
            self.bottom.push(new_element)
            print("A")
        else:
            self.top.push(new_element)
            print("B")

    def peek(self): # get the top of the queue
        return self.bottom.peek()

    def dequeue(self): # remove the top element from the queue
        item = self.bottom.pop()
        self.bottom = self.top
        self.top = Stack()
        while (self.bottom.peek() and self.bottom.top.next != None):
            self.top.push(self.bottom.pop())
        return item
    
    
q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
print(q.dequeue())