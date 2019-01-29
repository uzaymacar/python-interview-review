# QUESTION
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time Complexity: O(max(m, n)), Space Complexity: O(max(m, n)) where m and 
# n represents the length of l1 and l2 respectively.
class Solution:
    def constructNumber(self, node):
        str_num = ""
        while node:
            str_num = str(node.val) + str_num
            node = node.next
        return int(str_num)    
            
    def constructLinkedList(self, num):
        str_num = str(num)
        root = ListNode(str_num[-1])
        pointer = root
        for i in range(1, len(str_num)):
            pointer.next = ListNode(str_num[-1 - i])
            pointer = pointer.next
        return root
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.constructNumber(l1) # O(m)
        num2 = self.constructNumber(l2) # O(n)
        return self.constructLinkedList(num1 + num2) # O(m+n)


class Solution: # second solution with no unnecessary loops
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1 # node pointer for first linked list
        node2 = l2 # node pointer for second linked list
        lsum = None # node pointer for the summation linked list
        lsum_root = None # root node of summation linked list, to be returned
        carry = 0 # carried over for summation of digits
        
        while node1 or node2 or carry != 0: # don't forget carry !=0 for last digit
            val1 = 0 # initialize as 0
            val2 = 0 # initialize as 0
            if node1: # set to val only if pointer points to an existing node
                val1 = node1.val
            if node2: # set to val only if pointer points to an existing node
                val2 = node2.val
            
            digit_sum = val1 + val2 + carry # sum of digits + carry
            if digit_sum >= 10: # if exceeds 10, take mod and set carry
                digit_sum = digit_sum % 10
                carry = 1
            else: # else, no need for operation
                carry = 0
            
            if lsum_root == None: # if not existing, we set the root node
                lsum_root = ListNode(digit_sum)
                lsum = lsum_root
            else: # else, set next node and move on to next node
                lsum.next = ListNode(digit_sum)
                lsum = lsum.next
                
            if node1: # go to next node if not None
                node1 = node1.next
            if node2: # go to next node if not None
                node2 = node2.next
        
        return lsum_root

# TAKEAWAYS
# You can have helper methods inside a class.
# Remember to include the self keyword as a required positional argument in the declaration of class methods.
# Remember to call with self. when calling class methods.
# The first solution has unnecessary loops. You can minimize the number of loops, see second solution.
# The question will give away hints. The digits are stored in reverse order so we should probably do
# an in place summation for a quicker solution.
# BE CAREFUL: node = node.next, node = ListNode(<value>) is a very bad idea because you are essentially 
# setting a null (None) reference (node) to a ListNode without establishing any linked list connection. 
# The correct way would be to node.next = ListNode(<value>), and then move on to next with node = node.next.
# When approximated, the runtimes of both solutions will come as O(n+m) where the bigger value takes dominance,
# but with smaller sized linked lists, the second solution will operate slightly faster due to a single loop.
