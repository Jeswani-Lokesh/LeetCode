class Solution:
    def reverseBits(self, n: int) -> int:
         # This will store the reversed bits result
        result = 0

        # We must process exactly 32 bits
        for _ in range(32):
            # Shift result to the left to make space for the next bit
            result = result << 1

            # Get the last bit of n using AND with 1
            last_bit = n & 1

            # Add the last bit to result
            result = result | last_bit

            # Shift n to the right to process the next bit
            n = n >> 1

        # Return the final reversed number
        return result
        