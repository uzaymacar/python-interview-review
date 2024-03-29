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
    
# PRIORITY QUEUE IMPLEMENTATION
# Priority Queue is an extension of the queue with following properties.
# 1) An element with high priority is dequeued before an element with low priority.
# 2) If two elements have the same priority, they are served according to their order in the queue.
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): # method invoked with print() and str() calls/casts.
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == 0 
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on priority with O(N) time
    def delete(self): 
        try: 
            max_index = 0 # here priority is set according to largeness of an integer number
            for i in range(len(self.queue)): 
                if self.queue[i] > self.queue[max_index]: 
                    max_index = i 
            item = self.queue[max_index] 
            del self.queue[max_index] # to delete the item at max index
            return item 
        except IndexError: 
            print() 
            exit() 

# DIFFERENCE BETWEEN DEL, POP, AND REMOVE
# Use del to remove an element by index, pop() to remove it by index 
# if you NEED the returned value, and remove() to delete an element by value (first encountered)
# remove requires searching the list, and raises ValueError if no such value occurs in the list.

# When deleting index i from a list of n elements, 
#the computational complexities of these methods are
# del     O(n - i)
# pop     O(n - i)
# remove  O(n)

# Note that del (unlike pop) allows the removal of a range of indexes because of list slicing:
# lst = [3, 2, 2, 1]
# del lst[1:]
# lst -> [3]

# PRIORITY QUEUE TESTING
# myQueue = PriorityQueue() 
# myQueue.insert(12) 
# myQueue.insert(1) 
# myQueue.insert(14) 
# myQueue.insert(7) 
# print(myQueue)         
# while not myQueue.isEmpty(): 
    # print(myQueue.delete())