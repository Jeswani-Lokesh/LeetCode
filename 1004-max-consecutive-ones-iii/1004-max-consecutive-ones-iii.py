class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Left pointer of the window
        left = 0

        # Count of zeros in the current window
        zero_count = 0

        # Maximum length found
        max_length = 0

        # Expand the window using right pointer
        for right in range(len(nums)):

            # If current element is 0, increase zero count
            if nums[right] == 0:
                zero_count += 1

            # If zeros exceed k, shrink window from left
            while zero_count > k:
                # If left element is 0, reduce zero count
                if nums[left] == 0:
                    zero_count -= 1

                # Move left pointer forward
                left += 1

            # Update maximum length of valid window
            max_length = max(max_length, right - left + 1)

        # Return the maximum length
        return max_length