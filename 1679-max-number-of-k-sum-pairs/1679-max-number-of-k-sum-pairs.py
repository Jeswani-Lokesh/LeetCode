class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Sort the array
        nums.sort()

        # Left pointer
        left = 0

        # Right pointer
        right = len(nums) - 1

        # Count of valid pairs
        count = 0

        # Loop while pointers do not cross
        while left < right:
            # Current sum
            total = nums[left] + nums[right]

            # If sum equals k, we found a pair
            if total == k:
                count += 1
                # Move both pointers
                left += 1
                right -= 1

            # If sum is smaller, move left to increase sum
            elif total < k:
                left += 1

            # If sum is larger, move right to decrease sum
            else:
                right -= 1

        # Return total number of pairs
        return count