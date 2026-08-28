class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:              # note: `<`, not `<=`
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # Minimum is strictly to the right of mid
                left = mid + 1
            else:
                # Minimum is at mid or to its left
                right = mid              # keep mid — it could BE the min
        
        # left == right → converged on the minimum
        return nums[left]