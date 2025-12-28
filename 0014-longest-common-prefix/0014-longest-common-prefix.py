class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: empty list
        if not strs:
            return ""

        # Loop through characters of first string
        for i in range(len(strs[0])):
            char = strs[0][i]  # Reference character

            # Check same position i in all other strings
            for s in strs[1:]:
                # If index out of range or char doesn't match
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]  # Return prefix up to mismatch

        # If no mismatch, return entire first string
        return strs[0]
        