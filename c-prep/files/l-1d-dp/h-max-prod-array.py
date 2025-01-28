"""
152. Maximum Product Subarray

Given an integer array nums, find a 
subarray
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos_max = nums[0]
        neg_min = nums[0]
        max_prod = nums[0]

        idx = 1
        while idx < len(nums):
            curr = nums[idx]
            current_pos_max_prod = pos_max*curr
            current_neg_min_prod = neg_min*curr
            pos_max = max(curr, current_pos_max_prod, current_neg_min_prod)
            neg_min = min(curr, current_pos_max_prod, current_neg_min_prod)
            max_prod = max(pos_max, max_prod)
            idx += 1
        return max_prod

            