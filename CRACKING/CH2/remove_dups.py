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

my_list = LinkedList(Element(5))
my_list.append(Element(4))
my_list.append(Element(3))
my_list.append(Element(4))
my_list.append(Element(10))
my_list.append(Element(5))

# O(N)

def remove_dups(ll):
    counter = 1
    buf = []
    #delete_indexes = []
    while ll.get_position(counter) != None:
        val = ll.get_position(counter).get_value()
        print(counter, val)
        if val in buf:
            ll.delete_position(counter) # remember to add deletion
            #delete_indexes.append(counter)
        else:
            buf.append(val) # only append if newly seen
            counter += 1 # only increment counter if you are not deleting for proper order
    print(buf)
    #print(delete_indexes)
    #deletion = 0
    #for index in delete_indexes:
        #ll.delete_position(index - deletion)
        #deletion += 1

remove_dups(my_list)

for i in range(1, 5):
    print(my_list.get_position(i).get_value())