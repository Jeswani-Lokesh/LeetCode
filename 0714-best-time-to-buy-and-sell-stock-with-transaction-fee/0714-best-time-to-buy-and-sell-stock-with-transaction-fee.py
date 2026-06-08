class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Max profit when we do NOT hold a stock
        cash = 0

        # Max profit when we DO hold a stock
        hold = -prices[0]

        # Process prices from day 1 onward
        for i in range(1, len(prices)):
            # Current stock price
            price = prices[i]

            # Save old cash before updating it
            old_cash = cash

            # Option 1: keep not holding
            # Option 2: sell today and pay fee
            cash = max(cash, hold + price - fee)

            # Option 1: keep holding
            # Option 2: buy today using old cash
            hold = max(hold, old_cash - price)

        # Final answer must be cash because holding stock is unrealized profit
        return cash