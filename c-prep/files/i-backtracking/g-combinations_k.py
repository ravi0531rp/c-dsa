from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i):
            if len(sol) == k:
                res.append(sol[:])
                return 
            if i > n:
                return 

            curr_len = len(sol)
            left_to_complete = k - curr_len
            if n - i + 1 < left_to_complete:
                return 

            backtrack(i + 1)

            sol.append(i)
            backtrack(i + 1)
            sol.pop()

            

        backtrack(1)
        return res
