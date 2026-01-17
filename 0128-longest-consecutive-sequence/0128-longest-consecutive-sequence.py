class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to set for O(1) lookups
        num_set = set(nums)

        longest = 0

        for num in num_set:
            # Only start counting if num is the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                # Expand the sequence forward
                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
