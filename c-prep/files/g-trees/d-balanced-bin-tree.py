"""
Balanced Binary Tree

Given a binary tree, determine if it is 
height-balanced

"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isBalanced(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    is_balanced = [True]
    def get_height(node):
        if node is None:
            return 0
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        if abs(left_height - right_height) > 1:
            is_balanced[0] = False
        return 1 + max(left_height, right_height)
    get_height(root)
    return is_balanced[0]