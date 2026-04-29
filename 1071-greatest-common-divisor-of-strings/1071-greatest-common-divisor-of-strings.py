class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # If concatenating in different orders gives different results,
        # then there is no common divisor string
        if str1 + str2 != str2 + str1:
            return ""

        # Helper function to find GCD of two numbers
        def gcd(a, b):
            # Use Euclidean algorithm
            while b != 0:
                a, b = b, a % b
            return a

        # Find GCD of lengths of the two strings
        length = gcd(len(str1), len(str2))

        # Return the substring of str1 of that length
        return str1[:length]