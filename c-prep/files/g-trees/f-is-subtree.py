"""
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if 
there is a subtree of root with the same structure and node values of subRoot 
and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and 
all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.

"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and root2 and root1.val == root2.val:
            return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if subRoot is None:
            return True
        if self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)