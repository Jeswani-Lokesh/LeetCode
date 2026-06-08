class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Count total flips needed
        flips = 0

        # Check 32 bits
        for i in range(32):
            # Get i-th bit of a
            bit_a = (a >> i) & 1

            # Get i-th bit of b
            bit_b = (b >> i) & 1

            # Get i-th bit of c
            bit_c = (c >> i) & 1

            # If c bit is 1
            if bit_c == 1:
                # At least one of a or b must be 1
                if bit_a == 0 and bit_b == 0:
                    flips += 1

            # If c bit is 0
            else:
                # Both a and b must be 0
                if bit_a == 1:
                    flips += 1

                if bit_b == 1:
                    flips += 1

        # Return minimum flips
        return flips