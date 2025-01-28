"""
994. Rotting Oranges
Solved
Medium
Topics
Companies
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        num_fresh = 0
        minutes_passed = -1

        m, n = len(grid), len(grid[0])

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == FRESH:
                    num_fresh += 1
                elif grid[i][j] == ROTTEN:
                    queue.append((i,j))
        
        if not num_fresh:
            return 0
        
        while queue:
            minutes_passed += 1
            size = len(queue)

            for _ in range(size):
                i, j = queue.popleft()
                for r,c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        queue.append((r,c))
                        num_fresh -= 1
        return minutes_passed if not num_fresh else -1
                