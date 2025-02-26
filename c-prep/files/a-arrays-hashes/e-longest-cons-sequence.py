"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_len = 1
        curr_len = 1
        i = 1
        curr_val = nums[0]
        while i < len(nums):
            if nums[i] == curr_val + 1:
                curr_val = nums[i]
                curr_len += 1
                max_len = max(curr_len, max_len)
            elif nums[i] == curr_val:
                curr_val = nums[i]
            else:
                curr_len = 1
                curr_val = nums[i]
            
            i += 1
        return max_len
