# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            # Empty subtree is trivially valid
            if not node:
                return True
            
            # Current node must lie strictly within (low, high)
            if node.val <= low or node.val >= high:
                return False
            
            # Left subtree: upper bound tightens to node.val
            # Right subtree: lower bound tightens to node.val
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root, float('-inf'), float('inf'))