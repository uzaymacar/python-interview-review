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

my_list = LinkedList(Element(1))
my_list.append(Element(2))
my_list.append(Element(3))
#my_list.append(Element("o"))
my_list.append(Element(4))
#my_list.append(Element("a"))
#my_list.append(Element("t"))
#my_list.append(Element("t"))

my_list2 = LinkedList(my_list.get_position(1))
my_list2.append(Element(9))
my_list2.append(Element(2))

# def is_intersection(ll1, ll2):  
    # intersects = False
    # current1 = ll1.head
    # current2 = ll2.head
    
    # while current1 and current2:
        # if current1 == current2:
            # intersects = True
        # current1 = current1.next
        # current2 = current2.next
    
    # return intersects

def get_intersection(ll1, ll2): # show shared reference nodes by the same "ball" figure on paper to not get confused
    len1 = ll1.get_length()
    len2 = ll2.get_length()
    current_long = None
    current_short = None
    
    if len1 > len2:
        current_long = ll1.head
        current_short = ll2.head
    else:
        current_short = ll1.head
        current_long = ll2.head
    
    # In linked lists, nodes have only 1 next value, and therefore this approach works
    for i in range(abs(len1-len2)): # move the longer current node by difference
        current_long = current_long.next 
    
    while current_short != current_long:
        current_short = current_short.next
        current_long = current_long.next
    
    return current_short

print(get_intersection(my_list, my_list2).get_value())
        