# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Queue for BFS traversal
        queue = deque()

        # Add root node to queue
        queue.append(root)

        # Current level number starts at 1
        level = 1

        # Best level found so far
        best_level = 1

        # Maximum sum found so far
        max_sum = root.val

        # Process the tree level by level
        while queue:
            # Number of nodes in the current level
            level_size = len(queue)

            # Sum of current level
            current_sum = 0

            # Process all nodes in this level
            for i in range(level_size):
                # Remove one node from the queue
                node = queue.popleft()

                # Add node value to current level sum
                current_sum += node.val

                # Add left child if it exists
                if node.left:
                    queue.append(node.left)

                # Add right child if it exists
                if node.right:
                    queue.append(node.right)

            # If current level sum is greater than max_sum
            if current_sum > max_sum:
                # Update maximum sum
                max_sum = current_sum

                # Update best level
                best_level = level

            # Move to next level
            level += 1

        # Return level with maximum sum
        return best_level
        