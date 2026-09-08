# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current):
            if not node:
                return 0
            
            # Extend the number with this node's digit
            current = current * 10 + node.val
            
            # Leaf → the accumulated number is complete
            if not node.left and not node.right:
                return current
            
            # Internal node → sum both subtrees' contributions
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)
        