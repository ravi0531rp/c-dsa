"""
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), 
find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the 
lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]
        def search(root):
            if not root:
                return
            lca[0] = root
            if root.val in [p.val, q.val]:
                return
            if root.val > p.val and root.val > q.val:
                search(root.left)
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            else:
                return
        search(root)
        return lca[0]
