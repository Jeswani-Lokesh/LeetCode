class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # Calculate total sum of the array
        total_sum = sum(nums)

        # This will store the sum of elements on the left
        left_sum = 0

        # Loop through each index
        for i in range(len(nums)):

            # Calculate right sum using formula
            right_sum = total_sum - left_sum - nums[i]

            # Check if left sum equals right sum
            if left_sum == right_sum:
                return i

            # Add current element to left sum
            left_sum += nums[i]

        # If no pivot index found
        return -1