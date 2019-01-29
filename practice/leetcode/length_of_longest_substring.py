# QUESTION
# Given a string, find the length of the longest substring without repeating characters.
# Examples: "abcabcbb" -> 3, "bbbbb" -> 1, "pwwkew" -> 3, "dvdf" -> 3

# Time Complexity: O(N), Space Complexity: O(num_chars = 128) ~ O(1)
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # The ASCII table has 128 characters, with values from 0 through 127. [MAX = 128]
        # However, most computers typically reserve 1 byte (8 bits). [MAX = 256]
        
        num_chars = 128 # number of characters for ASCII values
        hash_map = [-1] * num_chars # hash_map to map characters within a string
        max_len = 0 # maximum substring length
        begin_index = 0 # beginning index for sliding window, start from 0
        
        for end_index in range(len(s)):
            char = s[end_index] # get the char at end_index
            if hash_map[ord(char)] != -1: # if seen before
                if hash_map[ord(char)] > begin_index: # if index stored is greater than begin_index
                    begin_index = hash_map[ord(char)] # set begin_index to the index stored
            new_len = end_index - begin_index + 1 # set new found substring length 
            if new_len > max_len: # if new found substring length is greater than max length
                max_len = new_len # set max length to new length
            hash_map[ord(char)] = end_index + 1 # map the char to its index + 1
            
        return max_len # return the maximum length archived at the end  

# TAKEAWAYS
# Sometimes starting with the naive brute force approach (O(N^3)) will help you solve the problem intuitively, and
# then you can try to optimize your solution accordingly.
# We only need to find the substring BETWEEN the repeated characters. If repeating characters are BACK TO BACK, the
# solution is a lot easier. In this solution, we map the character with the index it is in plus (+)  1 inside a hash
# map. This is sufficient for the problem. Don't forget to calculate new length as end index minus (-) beginning index
# plus (+1). In the case of a repeated character, we only update the hashmap after we have done the calculation
# to get the correct length.
# As more general takeaways, always try your solution multiple and differing inputs and try to cover some edge cases
# as well. Most often, there will be an edge case that you have forgotten. After writing your code, always
# go through it with a few sample tests to ensure it is indeed correctly working.
# This solution in particular is called the 'Sliding Window' and it comes in handy with searches in arrays and strings,
# especially when we want to solve the problem with a single pass through the structure (O(N) time complexity).
