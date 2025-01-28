"""

53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
from typing import List

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -1*float('inf')
        curr_sum = 0
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):

            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum, nums[i])
            if curr_sum < 0:
                curr_sum = 0
            
        return max_sum