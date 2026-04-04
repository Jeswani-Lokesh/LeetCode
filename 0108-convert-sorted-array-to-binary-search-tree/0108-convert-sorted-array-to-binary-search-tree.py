# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Helper function to build BST from part of the array
        def build(left, right):
            # If left index becomes greater than right index,
            # there are no elements left, so return None
            if left > right:
                return None

            # Find the middle index
            mid = (left + right) // 2

            # Create a tree node using the middle value
            root = TreeNode(nums[mid])

            # Build the left subtree using left half of the array
            root.left = build(left, mid - 1)

            # Build the right subtree using right half of the array
            root.right = build(mid + 1, right)

            # Return the root of this subtree
            return root

        # Start building the tree from the full array
        return build(0, len(nums) - 1)
        