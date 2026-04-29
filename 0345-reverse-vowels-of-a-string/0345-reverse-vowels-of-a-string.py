class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert string to list (strings are immutable)
        s = list(s)

        # Set of vowels for quick lookup
        vowels = set("aeiouAEIOU")

        # Left pointer
        left = 0

        # Right pointer
        right = len(s) - 1

        # Loop until pointers meet
        while left < right:

            # Move left pointer until it finds a vowel
            while left < right and s[left] not in vowels:
                left += 1

            # Move right pointer until it finds a vowel
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap the vowels
            s[left], s[right] = s[right], s[left]

            # Move both pointers inward
            left += 1
            right -= 1

        # Convert list back to string and return
        return "".join(s)
        