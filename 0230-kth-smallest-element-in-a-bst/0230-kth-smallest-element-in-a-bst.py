# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        curr = root
        
        while stack or curr:
            # Descend to the leftmost node, stacking the path
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Visit the node (this is the next value in sorted order)
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val      # reached the k-th smallest → stop
            
            # Move into the right subtree
            curr = curr.right
        
        return -1   # k out of range (shouldn't happen per constraints)
        