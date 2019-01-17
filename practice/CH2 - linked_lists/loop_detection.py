# LINKED LIST IMPLEMENTATION
class Element(object): # single unit (Node) in a linked list
    def __init__(self, value = None): # to initialize a new element
        self.value = value
        self.next = None
    
    def get_value(self): # get value (data) of element
        return self.value
        
class LinkedList(object):
    def __init__(self, head = None): # if we initialize a new LinkedList without a head, default head to None. 
        self.head = head
    
    def get_length(self):
        count = 0
        node = self.head
        while node:
            node = node.next
            count += 1
        return count
    
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
    
    def delete_working(self, d):
        n = self.head
        
        if n.value == d:
            return self.head.next
        
        while n.next:
            if n.next.value == d:
                n.next = n.next.next
                return self.head
            n = n.next
        
        return self.head     
    
    def delete_position(self, pos):
        counter = 1
        current = self.head
        prev = None
        while current.next and counter != pos:
            prev = current
            current = current.next
            counter += 1
        
        prev.next = current.next
        
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

my_list = LinkedList(Element("A"))
my_list.append(Element("B"))
my_list.append(Element("C"))
#my_list.append(Element("o"))
my_list.append(Element("D"))
my_list.append(my_list.get_position(3))
#my_list.append(Element("a"))
#my_list.append(Element("t"))
#my_list.append(Element("t"))

# Given a circular linked list, implement an algorithm that returns the node at
# the beginning of the loop.
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an
# earlier node, so as to make a loop in the linked list.

# Here is the summary for in:
# list - Average: O(n)
# set/dict - Average: O(1), Worst: O(n)
# The O(n) worst case for sets and dicts is very uncommon, 
# but it can happen if __hash__ is implemented poorly. 
# This only happens if everything in your set has the same hash value.

# O(N) # always think about fast and slow in sets

def has_loop(ll):
    # seen = [] # since in with lists take O(N), lets use a set
    seen = set()
    current = ll.head
    while current:
        if current in seen:
            return current
        seen.add(current)
        current = current.next
    
    return None

def has_loop_efficient(ll): # same run-time complexity, better space-time complexity O(1)
    fast = slow = ll.head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    
    if fast == None or fast.next == None:
        return None
    
    slow = ll.head 
    while fast != slow:
        slow = slow.next
        fast = fast.next
   
    return fast

# ALWAYS WRITE DIFFERENT TEST CASES AND LOOK FOR SPECIAL CASES
# 1) try with odd and even lengths
# 2) try with odd and even differences
print(has_loop_efficient(my_list).get_value())