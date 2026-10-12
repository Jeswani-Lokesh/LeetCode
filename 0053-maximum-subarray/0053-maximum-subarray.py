class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = best = nums[0]
        
        for num in nums[1:]:
            # Extend the previous subarray, or restart at num
            current = max(num, current + num)
            best = max(best, current)
        
        return best
        