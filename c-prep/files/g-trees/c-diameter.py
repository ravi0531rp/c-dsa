"""
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    max_diameter = [0] # python trick to access this value inside get_height
    if root is None:
        return 0
    def get_height(node):
        if node is None:
            return 0
        left_height = get_height(node.left)
        right_height = get_height(node.right)

        max_diameter[0] = max(max_diameter[0], left_height + right_height)

        return 1 + max(left_height, right_height)
    get_height(root)
    return max_diameter[0]