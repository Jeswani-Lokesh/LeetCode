class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         # This will store the potential majority element
        candidate = None

        # Counter used for voting
        count = 0

        # Traverse through the array
        for num in nums:
            # If count is zero, choose a new candidate
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                # Same as candidate → strengthen vote
                count += 1
            else:
                # Different from candidate → cancel one vote
                count -= 1

        # Since majority element is guaranteed to exist,
        # candidate will always be the correct answer
        return candidate
        