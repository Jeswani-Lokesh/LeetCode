class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort potions so we can use binary search
        potions.sort()

        # Store the final answer
        result = []

        # Number of potions
        n = len(potions)

        # Go through every spell
        for spell in spells:
            # Left pointer for binary search
            left = 0

            # Right pointer for binary search
            right = n - 1

            # This will store first potion index that works
            first_success = n

            # Binary search for smallest valid potion
            while left <= right:
                # Find middle index
                mid = (left + right) // 2

                # Check if spell with this potion reaches success
                if spell * potions[mid] >= success:
                    # This potion works, save index
                    first_success = mid

                    # Try to find smaller working potion on left side
                    right = mid - 1

                else:
                    # Potion too small, move right
                    left = mid + 1

            # Number of successful potions
            count = n - first_success

            # Add count to result
            result.append(count)

        # Return answer for all spells
        return result
        