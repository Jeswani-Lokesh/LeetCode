class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Set of vowels for quick lookup
        vowels = set("aeiou")

        # Count vowels in the first window
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1

        # Store maximum vowels seen so far
        max_count = count

        # Slide the window
        for i in range(k, len(s)):
            # Add new character (right side of window)
            if s[i] in vowels:
                count += 1

            # Remove old character (left side of window)
            if s[i - k] in vowels:
                count -= 1

            # Update maximum
            if count > max_count:
                max_count = count

        # Return the maximum vowels found
        return max_count
        