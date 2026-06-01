class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Left pointer starts at first index
        left = 0

        # Right pointer starts at last index
        right = len(nums) - 1

        # Keep searching until left and right meet
        while left < right:
            # Find middle index
            mid = (left + right) // 2

            # If mid is smaller than next element,
            # we are going uphill, so peak is on the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1

            # Otherwise, we are going downhill,
            # so peak is at mid or on the left
            else:
                right = mid

        # When left == right, that index is a peak
        return left
        