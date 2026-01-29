# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []

        def dfs(node, depth):
            if not node:
                return

            # Create new level if needed
            if depth == len(levels):
                levels.append([])

            levels[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        # Compute averages
        result = []
        for level in levels:
            result.append(sum(level) / len(level))

        return result
        