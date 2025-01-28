"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

"""
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)  
        parents = [i for i in range(n)]  
        rank = [1] * n  

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])  
            return parents[node]
        
        def union(node1, node2):
            par1, par2 = find(node1), find(node2)

            if par1 == par2:  
                return 0
            if rank[par1] > rank[par2]:
                parents[par2] = par1
                rank[par1] += rank[par2]
            else :
                parents[par1] = par2
                rank[par2] += rank[par1]
            return 1

        provinces = n

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:  
                    provinces -= union(i, j) 

        return provinces