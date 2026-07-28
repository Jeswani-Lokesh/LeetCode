class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2
        memo = {}

        def dfs(i, cur_sum):

            if cur_sum == target:
                return True

            if i == len(nums) or cur_sum > target:
                return False

            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            memo[(i, cur_sum)] = (
                dfs(i + 1, cur_sum + nums[i]) or
                dfs(i + 1, cur_sum)
            )

            return memo[(i, cur_sum)]

        return dfs(0, 0)