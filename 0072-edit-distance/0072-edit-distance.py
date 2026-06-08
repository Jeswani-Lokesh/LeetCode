class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Length of word1
        m = len(word1)

        # Length of word2
        n = len(word2)

        # Previous row represents dp[i - 1][j]
        prev = [0] * (n + 1)

        # Base case: convert empty word1 to word2
        for j in range(n + 1):
            prev[j] = j

        # Process each character in word1
        for i in range(1, m + 1):
            # Current row
            curr = [0] * (n + 1)

            # Base case: convert word1[0:i] to empty word2
            curr[0] = i

            # Process each character in word2
            for j in range(1, n + 1):

                # If characters match
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]

                else:
                    # Insert operation
                    insert_op = curr[j - 1]

                    # Delete operation
                    delete_op = prev[j]

                    # Replace operation
                    replace_op = prev[j - 1]

                    # Best operation + 1
                    curr[j] = 1 + min(
                        insert_op,
                        delete_op,
                        replace_op
                    )

            # Move current row to previous row
            prev = curr

        # Final answer
        return prev[n]