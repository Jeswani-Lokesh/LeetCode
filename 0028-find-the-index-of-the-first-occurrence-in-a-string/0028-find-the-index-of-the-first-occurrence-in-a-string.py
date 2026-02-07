class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is empty, it is found at index 0
        if needle == "":
            return 0

        # Length of haystack string
        n = len(haystack)

        # Length of needle string
        m = len(needle)

        # Loop through haystack where needle can fully fit
        for i in range(n - m + 1):
            # Check if substring starting at i matches needle
            if haystack[i:i + m] == needle:
                # If match found, return the index
                return i

        # If no match found, return -1
        return -1
        