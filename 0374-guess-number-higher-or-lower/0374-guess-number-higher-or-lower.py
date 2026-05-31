# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Start of search range
        left = 1

        # End of search range
        right = n

        # Keep searching while range is valid
        while left <= right:
            # Pick middle number
            mid = (left + right) // 2

            # Ask API about our guess
            result = guess(mid)

            # If result is 0, we found the answer
            if result == 0:
                return mid

            # If result is -1, our guess is too high
            elif result == -1:
                right = mid - 1

            # If result is 1, our guess is too low
            else:
                left = mid + 1
        