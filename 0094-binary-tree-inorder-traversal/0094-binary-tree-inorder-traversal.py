# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)          # Visit left subtree
            result.append(node.val) # Visit current node
            dfs(node.right)         # Visit right subtree

        dfs(root)
        return result
        