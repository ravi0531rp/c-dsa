"""
11. Container With Most Water

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line 
are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        p1, p2 = 0, len(height) - 1
        while p1 < p2:
            curr_vol =  min(height[p1], height[p2]) * abs(p1 - p2) # vol calculation
            max_vol = max(curr_vol, max_vol)
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
        return max_vol
            
        