"""
133. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}
        stack = [node]
        seen = set()
        seen.add(node)

        while stack:
            curr = stack.pop()
            if curr not in old_to_new:
                old_to_new[curr] = Node(val=curr.val)
            for neighbor in curr.neighbors:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

        for old_node, new_node in old_to_new.items():
            new_node.neighbors = [old_to_new[neighbor] for neighbor in old_node.neighbors]

        return old_to_new[node]
        