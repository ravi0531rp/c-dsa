"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

"""
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(start, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            
            if curr_sum > target:
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                sol.append(candidates[i])
                backtrack(i + 1, curr_sum + candidates[i])
                sol.pop()
        
        backtrack(0, 0)
        return res
