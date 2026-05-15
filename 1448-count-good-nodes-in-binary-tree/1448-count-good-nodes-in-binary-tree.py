# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS helper function
        def dfs(node, max_so_far):

            # If node is empty
            if node is None:
                return 0

            # Count of good nodes from this subtree
            count = 0

            # If current node is good
            if node.val >= max_so_far:
                count = 1

            # Update maximum value seen so far
            new_max = max(max_so_far, node.val)

            # Check left subtree
            count += dfs(node.left, new_max)

            # Check right subtree
            count += dfs(node.right, new_max)

            # Return total count
            return count

        # Start DFS from root
        return dfs(root, root.val)
