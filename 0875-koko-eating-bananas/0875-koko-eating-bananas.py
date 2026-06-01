class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Lowest possible eating speed
        left = 1

        # Highest possible eating speed
        right = max(piles)

        # Store the best answer found
        answer = right

        # Binary search over possible speeds
        while left <= right:
            # Try middle speed
            mid = (left + right) // 2

            # Total hours needed at speed mid
            hours = 0

            # Check each pile
            for pile in piles:
                # Add hours needed for this pile
                # This is ceiling division without using math.ceil
                hours += (pile + mid - 1) // mid

            # If Koko can finish within h hours
            if hours <= h:
                # mid is a possible answer
                answer = mid

                # Try smaller speed
                right = mid - 1

            # If Koko needs too many hours
            else:
                # Speed is too slow, increase it
                left = mid + 1

        # Return minimum valid speed
        return answer
        