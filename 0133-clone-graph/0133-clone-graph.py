"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        visited = {}
        
        def dfs(curr):
            # If already cloned, return the existing clone from the hash map
            if curr in visited:
                return visited[curr]
            
            # Create a clone for the current node and store it
            clone = Node(curr.val)
            visited[curr] = clone
            
            # Recursively clone all neighbors and append them
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
            
        return dfs(node)
        