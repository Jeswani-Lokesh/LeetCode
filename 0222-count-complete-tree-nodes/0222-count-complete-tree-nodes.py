# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # If the current node is empty, there are 0 nodes
        if root is None:
            return 0

        # Count nodes in the left subtree
        left_count = self.countNodes(root.left)

        # Count nodes in the right subtree
        right_count = self.countNodes(root.right)

        # Total nodes = current node + left subtree + right subtree
        return 1 + left_count + right_count
        