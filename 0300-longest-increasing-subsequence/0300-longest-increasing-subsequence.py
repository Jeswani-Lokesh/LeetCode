class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:

            # Find insertion position
            index = bisect_left(tails, num)

            # Extend the LIS
            if index == len(tails):
                tails.append(num)

            # Replace existing tail
            else:
                tails[index] = num

        return len(tails)
        