class Solution:
    def numTilings(self, n: int) -> int:
        # Mod value required by the problem
        MOD = 10**9 + 7

        # If board size is 1
        if n == 1:
            return 1

        # If board size is 2
        if n == 2:
            return 2

        # Create DP array
        dp = [0] * (n + 1)

        # Empty board has 1 way
        dp[0] = 1

        # 2 x 1 board has 1 way
        dp[1] = 1

        # 2 x 2 board has 2 ways
        dp[2] = 2

        # Fill DP table from 3 to n
        for i in range(3, n + 1):
            # Apply recurrence relation
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        # Return answer for 2 x n board
        return dp[n]
        