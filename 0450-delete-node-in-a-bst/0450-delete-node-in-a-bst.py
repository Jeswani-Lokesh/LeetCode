# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # If tree is empty, nothing to delete
        if root is None:
            return None

        # If key is smaller than current node value, go left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # If key is larger than current node value, go right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # If key matches current node, delete this node
        else:
            # Case 1 and 2:
            # If there is no left child, return right child
            if root.left is None:
                return root.right

            # Case 1 and 2:
            # If there is no right child, return left child
            if root.right is None:
                return root.left

            # Case 3:
            # Node has both left and right children

            # Find smallest node in right subtree
            successor = root.right

            # Keep moving left to find minimum value
            while successor.left:
                successor = successor.left

            # Replace current node value with successor value
            root.val = successor.val

            # Delete successor node from right subtree
            root.right = self.deleteNode(root.right, successor.val)

        # Return updated root
        return root