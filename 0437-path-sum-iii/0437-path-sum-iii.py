# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Dictionary to store prefix sum counts
        prefix_count = {}

        # Empty path has sum 0
        prefix_count[0] = 1

        # DFS helper function
        def dfs(node, current_sum):
            # If node is empty, no path found
            if node is None:
                return 0

            # Add current node value to running sum
            current_sum += node.val

            # We need this previous prefix sum to form targetSum
            needed_sum = current_sum - targetSum

            # Count paths ending at current node
            count = prefix_count.get(needed_sum, 0)

            # Add current prefix sum before going deeper
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

            # Search left subtree
            count += dfs(node.left, current_sum)

            # Search right subtree
            count += dfs(node.right, current_sum)

            # Backtrack: remove current prefix sum before returning
            prefix_count[current_sum] -= 1

            # Return total paths found in this subtree
            return count

        # Start DFS from root with sum 0
        return dfs(root, 0)