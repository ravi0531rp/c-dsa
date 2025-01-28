"""
213. House Robber II

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are arranged 
in a circle. That means the first house is the neighbor of the last one. Meanwhile, 
adjacent houses have a security system connected, and it will automatically contact 
the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), 
because they are adjacent houses.

"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=3:
            return max(nums)
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for idx in range(2, len(nums) - 1):
            dp[idx] = max(nums[idx] + dp[idx - 2], dp[idx -1])
        way1_max = dp[-2]

        dp = [0] * (len(nums))
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])

        for idx in range(3, len(nums)):
            dp[idx] = max(nums[idx] + dp[idx - 2], dp[idx -1])
        return max(way1_max, dp[-1])