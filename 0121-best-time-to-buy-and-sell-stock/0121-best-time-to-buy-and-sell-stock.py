class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         # If prices list is empty, no transaction possible
        if not prices:
            return 0

        # Minimum price seen so far (best day to buy)
        min_price = prices[0]

        # Maximum profit achievable
        max_profit = 0

        # Start from day 1 (since we cannot sell before buying)
        for price in prices[1:]:
            # If current price is lower, update min_price
            if price < min_price:
                min_price = price
            else:
                # Calculate profit if selling today
                profit = price - min_price
                # Update maximum profit
                if profit > max_profit:
                    max_profit = profit

        return max_profit