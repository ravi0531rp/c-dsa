"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an 
integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            mid = (p1 + p2) // 2  
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                p2 = mid - 1  
            else:
                p1 = mid + 1  

        return -1 
