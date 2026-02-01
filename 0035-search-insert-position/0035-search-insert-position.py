class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
         # Left pointer at the start of the array
        left = 0

        # Right pointer at the end of the array
        right = len(nums) - 1

        # Keep searching while left pointer does not cross right pointer
        while left <= right:
            # Find the middle index
            mid = (left + right) // 2

            # If target is found at mid, return mid
            if nums[mid] == target:
                return mid

            # If target is smaller, search left half
            elif nums[mid] > target:
                right = mid - 1

            # If target is larger, search right half
            else:
                left = mid + 1

        # If target is not found, left is the insert position
        return left
        