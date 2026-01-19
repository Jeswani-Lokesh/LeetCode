class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         # If array has 2 or fewer elements, it's already valid
        if len(nums) <= 2:
            return len(nums)

        # k is the index to place the next valid element
        k = 2

        for i in range(2, len(nums)):
            # Only keep nums[i] if it does not create more than 2 duplicates
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k
        