# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Extract values of nodes for easier comparison
        parent_val = root.val
        p_val = p.val
        q_val = q.val

        # Case 1: Both nodes are smaller → LCA must be in left subtree
        if p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Case 2: Both nodes are greater → LCA must be in right subtree
        elif p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Case 3: Split → one node on each side, or one is the current node → current root is LCA
        else:
            return root