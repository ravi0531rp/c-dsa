"""
112. Path Sum
Solved
Easy
Topics
Companies
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def check_sum(node, curr_sum):
            if not node:
                return False
            curr_sum += node.val
            if not node.left and not node.right:
                return curr_sum == targetSum
            return check_sum(node.left, curr_sum) or check_sum(node.right, curr_sum)
        return check_sum(root, 0)
        