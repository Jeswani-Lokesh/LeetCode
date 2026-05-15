# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # List to store leaf values from first tree
        leaves1 = []

        # List to store leaf values from second tree
        leaves2 = []

        # Helper function to collect leaf values
        def collect_leaves(node, leaves):
            # If node is empty, stop
            if node is None:
                return

            # If node has no left and no right child, it is a leaf
            if node.left is None and node.right is None:
                # Add leaf value to the list
                leaves.append(node.val)

                # Stop here because leaf has no children
                return

            # Visit left subtree
            collect_leaves(node.left, leaves)

            # Visit right subtree
            collect_leaves(node.right, leaves)

        # Collect leaves from first tree
        collect_leaves(root1, leaves1)

        # Collect leaves from second tree
        collect_leaves(root2, leaves2)

        # Compare both leaf sequences
        return leaves1 == leaves2
        