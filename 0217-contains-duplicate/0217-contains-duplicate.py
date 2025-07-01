class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       # nums = {}
        s = set()
        for i in range(0,len(nums)):
            if nums[i] in s:

                return True
            s.add(nums[i])
                

        else:
            return False




        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):

        #         if nums[i] == nums [j]:
        #             return True
        # return False
