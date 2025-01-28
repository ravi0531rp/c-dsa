"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        idx = 3
        while idx < n + 1:
            ways[idx] = ways[idx-1] + ways[idx - 2]
            idx +=1
        return ways[-1]