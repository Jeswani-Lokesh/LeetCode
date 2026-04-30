class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Smallest value seen so far
        first = float('inf')

        # Second smallest value seen so far
        second = float('inf')

        # Go through each number in the array
        for num in nums:

            # If current number is smaller than first
            if num <= first:
                # Update first
                first = num

            # If current number is greater than first but smaller than second
            elif num <= second:
                # Update second
                second = num

            # If current number is greater than both first and second
            else:
                # We found a valid triplet
                return True

        # No triplet found
        return False