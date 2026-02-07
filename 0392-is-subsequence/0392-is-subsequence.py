class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointer for string s
        i = 0

        # Pointer for string t
        j = 0

        # Loop while both pointers are within their string lengths
        while i < len(s) and j < len(t):
            # If characters match
            if s[i] == t[j]:
                # Move pointer i to the next character in s
                i += 1

            # Always move pointer j to the next character in t
            j += 1

        # If we matched all characters in s, return True
        return i == len(s)
        