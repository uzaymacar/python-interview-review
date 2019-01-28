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
        num1 = self.constructNumber(l1)
        num2 = self.constructNumber(l2)
        return self.constructLinkedList(num1 + num2)

# TAKEAWAYS
# You can have helper methods inside a class.
# Remember to include the self keyword as a required positional argument in the declaration of class methods.
# Remember to call with self. when calling class methods.

# TO DO
# Check if there exists a more optimized solution!
