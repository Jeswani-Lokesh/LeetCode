class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for position to place non-zero
        insert_pos = 0

        # Loop through array
        for i in range(len(nums)):
            # If current element is not zero
            if nums[i] != 0:
                # Swap current element with insert_pos
                nums[i], nums[insert_pos] = nums[insert_pos], nums[i]

                # Move insert_pos forward
                insert_pos += 1
        