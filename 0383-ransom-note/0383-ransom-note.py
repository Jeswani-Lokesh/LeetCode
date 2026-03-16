class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create an empty dictionary to count letters in magazine
        letter_count = {}

        # Count each letter in magazine
        for char in magazine:
            # If the letter is already in the dictionary
            if char in letter_count:
                # Increase its count by 1
                letter_count[char] += 1
            else:
                # Otherwise, add it with count 1
                letter_count[char] = 1

        # Go through each letter in ransomNote
        for char in ransomNote:
            # If the letter is not in the dictionary
            # or its count is already 0, we cannot build the note
            if char not in letter_count or letter_count[char] == 0:
                return False

            # Use one occurrence of that letter
            letter_count[char] -= 1

        # If we successfully used all letters, return True
        return True
