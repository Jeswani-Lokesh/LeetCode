# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Store the maximum diameter found
        diameter = 0

        # Returns the height of the current subtree
        def dfs(node):
            nonlocal diameter

            # Empty subtree has height 0
            if not node:
                return 0

            # Height of left subtree
            left_height = dfs(node.left)

            # Height of right subtree
            right_height = dfs(node.right)

            # Diameter passing through this node
            diameter = max(diameter, left_height + right_height)

            # Return height of current subtree
            return 1 + max(left_height, right_height)

        # Start DFS
        dfs(root)

        return diameter
        