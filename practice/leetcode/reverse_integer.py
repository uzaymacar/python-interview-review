# QUESTION
# Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only store integers within 
# the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 
# 0 when the reversed integer overflows.

# Time Complexity: O(N = log10(x)) [N = number of digits], 
# Space Complexity: O(1)
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """     
        output = int(str(abs(x))[::-1]) # Python syntax makes life much easier
        output = output if x > 0 else -output # Python-style ternary operation
        
        if output > (2**31)-1 or output < -2**31: # always check any constraints given by problem
            return 0
        return output
    
    def tiring_reverse(self, x):
        """
        :type x: int
        :rtype: int
        """     
        output = "" # initialize as a string
        
        if x == 0: # always think/check base cases
            return 0
        
        num = abs(x)  
        
        while num > 0:
            digit = num % 10 # move through the number by taking mod 10 (gets last digit)
            output += str(digit) # cast digit to sring and append to output
            num = int(num / 10) # update the number by diving by 10
        
        
        output = int(output) if x > 0 else int(output) * -1 # aha, use the ternary operator
        
        if output > (2**31)-1 or output < -(2**31): # aha, check for any constraints
            return 0
        
        return output
    
# TAKEAWAYS
# 1) Make use of slick Python syntax, it is there for a reason. Plus, it can be a plus in interviews.
# 2) ALWAYS cover/check your base cases.
# 3) Read the question carefully for any constraints.
