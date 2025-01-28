"""
300. Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

"""
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        idx = 1
        inc_subseq = [nums[0]]

        while idx < n:
            if nums[idx] > inc_subseq[-1]:
                inc_subseq.append(nums[idx])
            else:
                for i in range(len(inc_subseq)):
                    if inc_subseq[i] >= nums[idx]:
                        inc_subseq[i] = nums[idx]
                        break
            idx +=1
        print(inc_subseq)
        return len(inc_subseq)

        