# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Start from the root node
        current = root

        # Continue until node becomes None
        while current is not None:

            # If current node value matches target
            if current.val == val:
                return current

            # If target is smaller, go left
            elif val < current.val:
                current = current.left

            # If target is larger, go right
            else:
                current = current.right

        # Value not found
        return None