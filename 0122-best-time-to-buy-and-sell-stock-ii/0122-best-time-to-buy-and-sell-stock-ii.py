class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         # This will store the total profit
        profit = 0

        # Start from day 1 and compare with previous day
        for i in range(1, len(prices)):
            # If today's price is greater than yesterday's price
            if prices[i] > prices[i - 1]:
                # Add the profit from this increase
                profit += prices[i] - prices[i - 1]

        # Return the final total profit
        return profit
        