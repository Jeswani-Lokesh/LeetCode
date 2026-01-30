# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # This will store the value of the previously visited node
        self.prev = None

        # This will store the minimum difference found so far
        self.min_diff = float('inf')

        # Define inorder traversal function
        def inorder(node):
            # If the node is empty, stop
            if node is None:
                return

            # Visit left subtree first
            inorder(node.left)

            # If we have seen a previous node
            if self.prev is not None:
                # Calculate difference between current and previous node
                diff = abs(node.val - self.prev)

                # Update minimum difference if smaller
                self.min_diff = min(self.min_diff, diff)

            # Update previous node value to current node value
            self.prev = node.val

            # Visit right subtree
            inorder(node.right)

        # Start inorder traversal from root
        inorder(root)

        # Return the minimum difference found
        return self.min_diff
        