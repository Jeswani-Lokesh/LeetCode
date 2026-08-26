class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findBound(nums, target, find_first=True)
        if first == -1:               # target absent → skip second search
            return [-1, -1]
        last = self.findBound(nums, target, find_first=False)
        return [first, last]

    def findBound(self, nums: List[int], target: int, find_first: bool) -> int:
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid            # record this match
                if find_first:
                    right = mid - 1     # keep searching LEFT half
                else:
                    left = mid + 1      # keep searching RIGHT half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result