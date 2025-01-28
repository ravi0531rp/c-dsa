"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        ans = [-1]
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            count[0] += 1

            if count[0] == k:
                ans[0] = node.val
                return

            dfs(node.right)
        dfs(root)
        return ans[0]
            
