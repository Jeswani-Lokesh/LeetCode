class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # This variable stores the farthest index we can reach so far
        farthest = 0

        # Loop through each index of the array
        for i in range(len(nums)):
            # If current index is greater than farthest reachable index,
            # it means we cannot even stand on this position
            if i > farthest:
                return False

            # Update the farthest position we can reach from here
            farthest = max(farthest, i + nums[i])

        # If we finish the loop, the last index is reachable
        return True
        