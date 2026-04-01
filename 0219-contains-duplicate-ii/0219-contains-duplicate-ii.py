class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the last index where each number appeared
        last_seen = {}

        # Loop through the array using index
        for i in range(len(nums)):
            # Current number
            num = nums[i]

            # If we have seen this number before
            if num in last_seen:
                # Check if the difference in indices is at most k
                if i - last_seen[num] <= k:
                    return True

            # Update the latest index of this number
            last_seen[num] = i

        # If no valid pair was found, return False
        return False
        