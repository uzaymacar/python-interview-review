# QUESTION
# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.
# Examples: "babad" -> "bab" or "aba", "cbbd" -> "bb"

# Time Complexity: O(N^2) [for each index, expand from center: O(N) * O(N)], 
# Space Complexity: O(1)
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start_index = 0 # start index of the palindrome
        end_index = 0 # end index of the palindrome
        
        # Feel free to use Python function len() wherever as it only costs O(1)
        for cur_index in range(len(s)):
            odd_len = self.expand_from_center(cur_index, cur_index, s) # check for odd length palindrome
            even_len = self.expand_from_center(cur_index, cur_index + 1, s) # check for even length palindrome
            max_len = max(odd_len, even_len) # get the maximum length found of the two
            if max_len > end_index - start_index: # if new found palindrome length greater than before
                start_index = cur_index - int((max_len - 1)/2)  # set new start_index accordingly
                end_index = cur_index + int(max_len/2) # set new end_index accordingly
    
        return s[start_index:end_index+1] # return the longest palindrome found
    
    def expand_from_center(self, left, right, s):
        """Helper function to simulate a sliding window to
           compute length of palindrome substring.           
        :type left: int -> representing the sliding left index
        :type right: int -> representing the sliding right index
        :type s: str -> input string as before
        :rtype: int -> return length of the palindrome substring
        """
        # Initialize left and right points as new variables to modify
        l = left 
        r = right
        # Loop until 1) left point didn't exceed the beginning index (0),
        # 2) right point didn't exceed the last index (len(s)), and
        # 3) palindrome rule (s[l] == s[r]) still counts
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
        # Normally we would have expected to return r - l + 1, but since
        # we decrement l and increment r while in, respectively, the first
        # and last index, we have added an additional length of 2 
        # which we need to count for: r - l + 1 - 2 = r - l - 1
        
# TAKEAWAYS
# 1) A sliding window with two sliders that both expand from the center index in the 
# case of a odd length palindrome, and one expanding from the left median while
# the other expanding from the right median in the case of an even length palindrome
# will give a good solution.
# 2) To notice how whilst calculating start_index we additionaly decrement max_len by 1,
# you will give to give test values. Be careful about indexing as a general rule!
# 3) Helper functions are always useful, both for modularizing your solution and
# recursive/iterative approaches.


