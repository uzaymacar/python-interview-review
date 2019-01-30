# QUESTION
# Determine whether an integer is a palindrome. An integer is a 
# palindrome when it reads the same backward as forward.

# Time Complexity: O(N = log10(x)) [N = number of digits],
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
    
    def isPalindromeTiring(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        stop = len(x_str)
        left = 0
        right = len(x_str) - 1
        while left <= len(x_str)//2:
            if x_str[left] != x_str[right]:
                return False
            left += 1
            right -= 1
        
        return True

# TAKEAWAYS
# 1) An engineer should always be lazy; try to solve the problem with minimum number of operations.
