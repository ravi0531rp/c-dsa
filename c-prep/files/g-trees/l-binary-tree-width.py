from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        max_width = 1
        while queue:
            _, curr_level = queue[0]
            length = len(queue)

            for _ in range(len(queue)):
                node, level = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*level))
                if node.right:
                    queue.append((node.right, 2*level + 1))
            max_width = max(max_width, level - curr_level + 1)
        return max_width
