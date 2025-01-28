"""
78. Subsets
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [] , []
        n = len(nums)

        def back_track(i):
            if i == n:
                res.append(sol[:])
                return

            # Case 1: Don't pick the number
            back_track(i+1)

            # Case 2: Pick
            sol.append(nums[i])
            back_track(i+1)
            sol.pop()

        back_track(0)
        return res