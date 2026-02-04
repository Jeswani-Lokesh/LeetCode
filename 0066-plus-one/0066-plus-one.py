class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit
        i = len(digits) - 1

        # Loop backwards through the list
        while i >= 0:
            # If the current digit is less than 9
            if digits[i] < 9:
                # Just add 1 to it
                digits[i] += 1
                # We are done, so return the result
                return digits
            else:
                # If digit is 9, it becomes 0
                digits[i] = 0
                # Move to the previous digit
                i -= 1

        # If we exit the loop, all digits were 9
        # Example: [9,9,9] → [1,0,0,0]
        digits.insert(0, 1)

        # Return the final result
        return digits
        