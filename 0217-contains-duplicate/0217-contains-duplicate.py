class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        #         else:
        #             return False
        if len(nums) != len(set(nums)):
            return True
        else:
            return False
            
        