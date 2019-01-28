# QUESTION
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time complexity: O(N), Space Complexity: O(N)
        seen = {} 
        for i in range(len(nums)):
            num = nums[i]
            wanted = target-num # don't take absolute value for negative values to work
            if wanted in seen.keys():
                return [seen[wanted], i]
            seen[num] = i
        return None

# TAKEAWAYS
# Test your solution for all edge cases, including negative and positive integers and zero.
# There are always multiple solutions to a problem. The optimal solution will change when you have low memory 
# (optimize space complexity) and when you have low processing power or a time limit (optimize time complexity).
