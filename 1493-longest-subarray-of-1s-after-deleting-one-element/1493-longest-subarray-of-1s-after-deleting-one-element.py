class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Left pointer of window
        left = 0

        # Count of zeros in current window
        zero_count = 0

        # Maximum window size
        max_length = 0

        # Expand window with right pointer
        for right in range(len(nums)):

            # If current element is zero, increase zero count
            if nums[right] == 0:
                zero_count += 1

            # If more than 1 zero, shrink window
            while zero_count > 1:
                # If left element is zero, decrease count
                if nums[left] == 0:
                    zero_count -= 1

                # Move left pointer
                left += 1

            # Update maximum length (window size)
            max_length = max(max_length, right - left + 1)

        # Subtract 1 because we must delete one element
        return max_length - 1