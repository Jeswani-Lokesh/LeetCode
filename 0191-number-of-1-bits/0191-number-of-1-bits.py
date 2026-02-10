class Solution:
    def hammingWeight(self, n: int) -> int:
        # This variable will count the number of 1 bits
        count = 0

        # Loop until the number becomes 0
        while n > 0:
            # Get the last bit of n
            # n & 1 is 1 if the last bit is 1, otherwise 0
            last_bit = n & 1

            # Add the last bit to count
            count += last_bit

            # Shift n to the right to remove the last bit
            n = n >> 1

        # Return the total number of 1 bits
        return count
        