class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0  # Indices for longest palindrome

        def expandAroundCenter(left: int, right: int) -> tuple[int, int]:
            # Expand as long as left == right
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return final valid bounds (non-inclusive on right)
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd length palindromes (centered at i)
            l1, r1 = expandAroundCenter(i, i)
            # Even length palindromes (centered between i and i+1)
            l2, r2 = expandAroundCenter(i, i + 1)

            # Update longest found
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
        