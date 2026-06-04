class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create DP grid
        dp = [[0] * n for _ in range(m)]

        # First row has only one path
        for col in range(n):
            dp[0][col] = 1

        # First column has only one path
        for row in range(m):
            dp[row][0] = 1

        # Fill remaining cells
        for row in range(1, m):
            for col in range(1, n):

                # Top + Left
                dp[row][col] = (
                    dp[row - 1][col] +
                    dp[row][col - 1]
                )

        # Bottom-right corner
        return dp[m - 1][n - 1]