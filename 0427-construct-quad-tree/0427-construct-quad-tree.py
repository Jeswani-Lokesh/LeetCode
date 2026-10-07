"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(r, c, size):
            # Check if the entire region [r..r+size) x [c..c+size) is uniform
            first = grid[r][c]
            uniform = True
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        uniform = False
                        break
                if not uniform:
                    break
            
            # Uniform region → leaf node
            if uniform:
                return Node(first == 1, True, None, None, None, None)
            
            # Otherwise split into 4 quadrants of half the size
            half = size // 2
            return Node(
                True,                              # val is arbitrary for internal nodes
                False,                             # isLeaf = False
                build(r,        c,        half),   # topLeft
                build(r,        c + half, half),   # topRight
                build(r + half, c,        half),   # bottomLeft
                build(r + half, c + half, half),   # bottomRight
            )
        
        return build(0, 0, len(grid))
        