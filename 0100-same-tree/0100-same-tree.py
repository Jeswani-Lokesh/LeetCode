# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
         # Base case: both nodes are None → trees match
        if not p and not q:
            return True

        # One is None, one isn't → trees differ
        if not p or not q:
            return False

        # Check current node values
        if p.val != q.val:
            return False

        # Recur for left and right subtrees
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
        