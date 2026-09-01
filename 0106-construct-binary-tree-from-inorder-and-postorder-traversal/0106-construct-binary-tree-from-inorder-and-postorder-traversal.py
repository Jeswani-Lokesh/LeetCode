# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) root lookup
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1   # consume postorder from the end
        
        def build(left, right):
            # No elements in this range → empty subtree
            if left > right:
                return None
            
            # The current last unused postorder value is this subtree's root
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            
            # Split inorder around the root
            mid = idx_map[root_val]
            
            # Build RIGHT before LEFT — postorder is consumed back-to-front,
            # so the root's right subtree comes before its left subtree.
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            
            return root
        
        return build(0, len(inorder) - 1)
        