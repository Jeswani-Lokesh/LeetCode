# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If root is empty, there is no ancestor
        if root is None:
            return None

        # If current node is p or q, return current node
        if root == p or root == q:
            return root

        # Search for p and q in the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search for p and q in the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are not None,
        # it means p and q were found on different sides
        if left is not None and right is not None:
            return root

        # If left side found something, return it
        if left is not None:
            return left

        # Otherwise return whatever right side found
        return right