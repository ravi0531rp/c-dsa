"""

560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number 
of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

"""
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_cnt = {0 : 1}
        count = 0
        curr_sum = 0
        for item in nums:
            curr_sum += item
            extra = curr_sum - k
            
            count += prefix_sum_cnt.get(extra, 0)
            prefix_sum_cnt[curr_sum] = 1 + prefix_sum_cnt.get(curr_sum, 0)
        return count
        
        