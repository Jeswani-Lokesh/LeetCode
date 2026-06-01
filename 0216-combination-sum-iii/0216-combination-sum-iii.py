class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # This list stores all valid combinations
        result = []

        # Helper function for backtracking
        def backtrack(start, current, remaining_sum):
            # If current combination has k numbers
            if len(current) == k:
                # Check if sum is exactly n
                if remaining_sum == 0:
                    # Add a copy of current combination
                    result.append(current[:])

                # Stop this path
                return

            # Try numbers from start to 9
            for num in range(start, 10):
                # If num is bigger than remaining sum, no need to continue
                if num > remaining_sum:
                    break

                # Choose current number
                current.append(num)

                # Move to next number because each number can be used once
                backtrack(num + 1, current, remaining_sum - num)

                # Undo choice
                current.pop()

        # Start from number 1 with empty combination
        backtrack(1, [], n)

        # Return all valid combinations
        return result
        