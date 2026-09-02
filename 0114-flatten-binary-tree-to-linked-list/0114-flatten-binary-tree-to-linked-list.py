# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """Flatten in place — no return."""
        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node of the left subtree (preorder predecessor
                # of curr's right subtree)
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # Splice: attach current right subtree after that rightmost node
                prev.right = curr.right
                # Move the left subtree to the right
                curr.right = curr.left
                curr.left = None
            
            # Advance down the newly-formed right chain
            curr = curr.right
        