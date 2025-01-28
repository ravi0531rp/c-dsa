"""
210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

"""
from collections import defaultdict
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = prerequisites
        graph = defaultdict(list)

        for u,v in courses:
            graph[u].append(v)
        

        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * (numCourses)
        order = []

        def dfs(node):
            if states[node] == VISITING:
                return False
            elif states[node] == VISITED:
                return True
            states[node] = VISITING
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            states[node] = VISITED
            order.append(node)
            return True


        for node in range(numCourses):
            if not dfs(node):
                return []
        return order