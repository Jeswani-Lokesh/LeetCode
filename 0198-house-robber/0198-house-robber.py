class Solution:
    def rob(self, nums: List[int]) -> int:
        # Best money up to two houses before
        prev2 = 0

        # Best money up to previous house
        prev1 = 0

        # Go through each house amount
        for money in nums:
            # Option 1: skip current house, keep prev1
            skip_current = prev1

            # Option 2: rob current house, add money to prev2
            rob_current = prev2 + money

            # Best answer up to current house
            current = max(skip_current, rob_current)

            # Move prev2 forward
            prev2 = prev1

            # Move prev1 forward
            prev1 = current

        # prev1 stores the best answer after all houses
        return prev1