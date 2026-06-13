class StockSpanner:

    def __init__(self):
        # Stack stores pairs: (price, span)
        # price = previous stock price
        # span = how many days this price already covers
        self.stack = []
        

    def next(self, price: int) -> int:
        # Today's span starts as 1
        span = 1

        # Merge all previous prices that are <= today's price
        while self.stack and self.stack[-1][0] <= price:
            # Pop previous price and its span
            previous_price, previous_span = self.stack.pop()

            # Add previous span to today's span
            span += previous_span

        # Push today's price with its total span
        self.stack.append((price, span))

        # Return today's span
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)