class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Edge case: empty list

        write = 1  # Position to write next unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write] = nums[i]  # Overwrite duplicate with unique
                write += 1             # Move write pointer

        return write  # Number of unique elements
        