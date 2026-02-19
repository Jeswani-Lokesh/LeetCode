class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # This will store the result
        result = 0

        # Go through every number in the list
        for num in nums:
            # XOR current number with result
            result = result ^ num

        # The remaining number is the answer
        return result
        