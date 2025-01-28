"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for idx in range(len(nums)):
            if idx > 0 and nums[idx-1] == nums[idx]: # to avoid repitition 
                continue
            pt1, pt2 = idx+1, len(nums) - 1 # now a regular 2 sum
            while pt1 < pt2:
                curr_sum = nums[pt1] + nums[pt2] + nums[idx]
                if curr_sum > 0:
                    pt2 -= 1
                elif curr_sum < 0:
                    pt1 +=1
                else: # our main case
                    results.append([nums[idx], nums[pt1], nums[pt2]])
                    pt1 += 1 # move the left pointer ->
                    while nums[pt1] == nums[pt1 - 1] and pt1 < pt2: # again keep moving to avaoid repitition
                        pt1 += 1

                
        return results