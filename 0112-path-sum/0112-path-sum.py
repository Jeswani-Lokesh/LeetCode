# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # If the tree is empty, no path exists
        if root is None:
            return False

        # If this is a leaf node
        if root.left is None and root.right is None:
            # Check if the remaining sum equals the node value
            return targetSum == root.val

        # Subtract the current node value from targetSum
        remaining_sum = targetSum - root.val

        # Check left subtree
        left_result = self.hasPathSum(root.left, remaining_sum)

        # Check right subtree
        right_result = self.hasPathSum(root.right, remaining_sum)

        # If either side returns True, a valid path exists
        return left_result or right_result