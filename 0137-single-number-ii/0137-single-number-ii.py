class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for bit in range(32):
            count = sum((num >> bit) & 1 for num in nums)
            if count % 3:
                result |= (1 << bit)
        
        # Python ints are unbounded: convert from 32-bit two's complement
        if result >= 1 << 31:
            result -= 1 << 32
        return result
        