class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:
                # LEFT half [left..mid] is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1     # target in the sorted left half
                else:
                    left = mid + 1      # target in the right half
            else:
                # RIGHT half [mid..right] is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1      # target in the sorted right half
                else:
                    right = mid - 1     # target in the left half
        
        return -1