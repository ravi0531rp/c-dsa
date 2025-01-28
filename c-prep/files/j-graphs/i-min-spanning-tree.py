"""
1584. Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
"""

import heapq
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        cost = 0
        heap = [(0,0)]

        while len(seen) < n:
            dist, idx = heapq.heappop(heap)
            if idx in seen:
                continue
            cost += dist
            seen.add(idx)

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    xi, yi = points[idx]
                    dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(heap, (dist, j))
        return cost