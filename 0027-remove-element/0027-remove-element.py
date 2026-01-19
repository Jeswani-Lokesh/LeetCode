class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                # Shift elements left
                for j in range(i + 1, n):
                    nums[j - 1] = nums[j]
                n -= 1
            else:
                i += 1

        return n
        