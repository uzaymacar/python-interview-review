# In Python arrays = lists pretty much. Arrays are easy to append 
# or search, lets say, but for insertions and deletions may get messy.

# Linked Lists [both singly(next) and doubly(next, prev)]
# on the other hand, have constant time O(1) for insertion and deletion.
# That is why they may be preferable.

# DONT USE && or || in Python, instead you can just use
# 'and' or 'or' keywords which makes life easier.

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

my_list = LinkedList(Element(5))
my_list.append(Element(4))
print(my_list.get_position(1).get_value())

# In Python, stack can be implemented with a list.
# append() = push() and pop() is already a built in function.
# STACKS ARE LAST IN FIRST OUT (LIFO)

# STACK IMPLEMENTATION USING LINKED LIST
class Stack(object):
    def __init__(self,top = None): # initiliaze with a LinkedList with top as its head
        self.ll = LinkedList(top)

    def push(self, new_element): # push to the top of the stack
        self.ll.insert_first(new_element) # notice when calling functions, we omit self
        # we think like 'self' is given, it will always be there so no need to resend it as a parameter

    def pop(self): # pop from the top of the stack
        return self.ll.delete_first()

# Creating a queue is very easy and ca be all done in 1 line.
# Don't forget to make use of already existing/built-in functions
# such as pop() : list.pop(index) -- removes and returns the element at the given index. 
# pop() returns the rightmost element if index is omitted (roughly the opposite of append()).
# QUEUES ARE FIRST IN FIRST OUT (FIFO)
        
# QUEUE IMPLEMENTATION USING STANDARD LIST
class Queue(object):
    def __init__(self, head = None): # initiliaze with a list containing head as its first element
        self.storage = [head]

    def enqueue(self, new_element): # append to the end of the queue
        self.storage.append(new_element)

    def peek(self): # get the top of the queue
        return self.storage[0]

    def dequeue(self): # remove the top element from the queue
        return self.storage.pop(0)