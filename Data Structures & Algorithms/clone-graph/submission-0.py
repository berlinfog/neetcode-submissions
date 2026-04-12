"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}
        if not node:
            return None
        def dfs(i):
            if i in oldtonew:
                return oldtonew[i]
            
            copy = Node(i.val)
            oldtonew[i] = copy

            for j in i.neighbors:
                copy.neighbors.append(dfs(j))
            
            return copy
        
        return dfs(node)
