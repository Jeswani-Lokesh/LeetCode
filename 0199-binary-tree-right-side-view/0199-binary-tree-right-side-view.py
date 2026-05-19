# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Final answer
        result = []

        # DFS helper
        def dfs(node, depth):

            # If node is empty
            if node is None:
                return

            # First node seen at this depth
            if depth == len(result):
                result.append(node.val)

            # Visit right side first
            dfs(node.right, depth + 1)

            # Visit left side
            dfs(node.left, depth + 1)

        # Start DFS
        dfs(root, 0)

        return result
        