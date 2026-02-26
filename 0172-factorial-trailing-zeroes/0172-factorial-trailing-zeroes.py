class Solution:
    def trailingZeroes(self, n: int) -> int:
        # This will store the final number of trailing zeros
        count = 0

        # Keep dividing n by 5 to count factors of 5
        while n > 0:
            # Divide n by 5 (how many multiples of 5 exist)
            n = n // 5

            # Add that amount to the count
            count += n

        # Return the total number of trailing zeros
        return count
        