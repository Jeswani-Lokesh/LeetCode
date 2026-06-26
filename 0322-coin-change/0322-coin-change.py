class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Infinity means amount cannot be formed yet
        dp = [float("inf")] * (amount + 1)

        # Zero coins needed to make amount 0
        dp[0] = 0

        # Compute answer for every amount
        for current_amount in range(1, amount + 1):

            # Try every coin
            for coin in coins:

                # Coin can contribute only if it does not exceed current amount
                if coin <= current_amount:

                    dp[current_amount] = min(
                        dp[current_amount],
                        dp[current_amount - coin] + 1
                    )

        # If still infinity, amount cannot be formed
        if dp[amount] == float("inf"):
            return -1

        return dp[amount]