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
        item = self.top.data
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
    
    def isNotEmpty(self):
        return self.top != None
        
# DOLDUR BOSALT TAKTIGINI UNUTMA. You can achieve this through the usage
# of a temporary stack
        
stack = Stack(StackNode(5))
stack.push(4)
stack.push(3)
stack.push(15)
stack.push(25)

def sort_smallest_on_top_stack(stack): # look again!
    temporary_stack = Stack()
    while not stack.isEmpty():
        temporary_item = stack.pop()
        while not temporary_stack.isEmpty() and temporary_stack.peek() < temporary_item: # change < with > for descending order
            popped_item = temporary_stack.pop()
            stack.push(popped_item)
        temporary_stack.push(temporary_item)
    return temporary_stack

sorted_stack = sort_smallest_on_top_stack(stack)
print(sorted_stack.peek())
for i in range(5):
    print(sorted_stack.pop())
        
        
