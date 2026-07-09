class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow
        if dividend == -(2 ** 31) and divisor == -1:
            return 2 ** 31 - 1

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Keep subtracting until dividend becomes smaller
        while dividend >= divisor:

            # Current multiple of divisor
            temp = divisor

            # Corresponding quotient contribution
            multiple = 1

            # Double temp while it still fits
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            # Remove the largest chunk
            dividend -= temp

            # Add to quotient
            quotient += multiple

        # Apply sign
        if negative:
            quotient = -quotient

        return quotient