class Solution:
    def climbStairs(self, n: int) -> int:
        # If n is 1, only one way
        if n == 1:
            return 1

        # If n is 2, two ways
        if n == 2:
            return 2

        # Ways to reach step 1
        prev1 = 1

        # Ways to reach step 2
        prev2 = 2

        # Calculate ways for steps from 3 to n
        for i in range(3, n + 1):
            # Current ways = previous two ways added
            current = prev1 + prev2

            # Move the window forward
            prev1 = prev2
            prev2 = current

        # prev2 now holds the answer
        return prev2
        