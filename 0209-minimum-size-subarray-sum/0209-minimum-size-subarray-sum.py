class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
         # Left pointer of the sliding window
        left = 0

        # Current sum of the window
        current_sum = 0

        # Set answer to a very large number initially
        min_length = float('inf')

        # Right pointer moves through the array
        for right in range(len(nums)):
            # Add the current number to the window sum
            current_sum += nums[right]

            # While current sum is enough (>= target)
            while current_sum >= target:
                # Calculate current window size
                window_length = right - left + 1

                # Update minimum length if smaller
                min_length = min(min_length, window_length)

                # Remove the leftmost number from the sum
                current_sum -= nums[left]

                # Move left pointer to shrink the window
                left += 1

        # If min_length was never updated, return 0
        if min_length == float('inf'):
            return 0

        # Otherwise, return the smallest length found
        return min_length
        