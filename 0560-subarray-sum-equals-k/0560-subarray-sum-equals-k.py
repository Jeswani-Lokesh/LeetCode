class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix_sum -> frequency
        prefix_count = {0: 1}

        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            # Check if a previous prefix sum forms sum k
            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]

            # Store current prefix sum
            prefix_count[prefix_sum] = (
                prefix_count.get(prefix_sum, 0) + 1
            )

        return count
        