"""
695. Max Area of Island
Solved
Medium
Topics
Companies
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0
"""
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i-1, j) + dfs(i, j - 1) + dfs(i+1, j) + dfs(i, j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(dfs(i,j), max_area)
        return max_area