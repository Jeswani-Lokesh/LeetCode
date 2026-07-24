class Solution:
    def maxProduct(self, nums: List[int]) -> int:
                # Initialize with the first element
        curMax = nums[0]
        curMin = nums[0]
        result = nums[0]

        # Process the remaining elements
        for i in range(1, len(nums)):
            num = nums[i]

            # Save current max before updating
            temp = curMax

            # Maximum product ending here
            curMax = max(num, num * curMax, num * curMin)

            # Minimum product ending here
            curMin = min(num, num * temp, num * curMin)

            # Update global answer
            result = max(result, curMax)

        return result
        