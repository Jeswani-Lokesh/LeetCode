class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []

        # Keep only alphanumeric characters
        for ch in s:
            if ch.isalnum():
                cleaned.append(ch.lower())

        # Compare string with its reverse
        return cleaned == cleaned[::-1]
        