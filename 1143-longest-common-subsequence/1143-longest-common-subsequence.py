class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Length of first string
        m = len(text1)

        # Length of second string
        n = len(text2)

        # Create DP table with extra row and column
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Loop through text1
        for i in range(1, m + 1):

            # Loop through text2
            for j in range(1, n + 1):

                # Current character from text1
                char1 = text1[i - 1]

                # Current character from text2
                char2 = text2[j - 1]

                # If characters match
                if char1 == char2:
                    # Add 1 to previous diagonal result
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                # If characters do not match
                else:
                    # Take best by skipping one character
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

        # Bottom-right cell has final answer
        return dp[m][n]