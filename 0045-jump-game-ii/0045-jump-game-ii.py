class Solution:
    def jump(self, nums: List[int]) -> int:
        # Number of jumps made
        jumps = 0

        # The end of the current jump range
        current_end = 0

        # The farthest index we can reach
        farthest = 0

        # Loop through array (no need to go till last index)
        for i in range(len(nums) - 1):
            # Update farthest we can reach
            farthest = max(farthest, i + nums[i])

            # If we reach the end of current range
            if i == current_end:
                # We must take a jump
                jumps += 1

                # Update the range for next jump
                current_end = farthest

        # Return total jumps
        return jumps
        