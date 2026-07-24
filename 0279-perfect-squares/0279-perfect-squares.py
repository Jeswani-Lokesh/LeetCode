class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def dfs(remain):

            if remain == 0:
                return 0

            if remain in memo:
                return memo[remain]

            ans = float("inf")

            i = 1
            while i * i <= remain:
                ans = min(ans, 1 + dfs(remain - i * i))
                i += 1

            memo[remain] = ans
            return ans

        return dfs(n)
        