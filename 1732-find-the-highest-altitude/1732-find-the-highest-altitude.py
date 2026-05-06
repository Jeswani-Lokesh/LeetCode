class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Current altitude starts at 0
        current_altitude = 0

        # Maximum altitude seen so far
        max_altitude = 0

        # Go through each gain value
        for g in gain:
            # Update current altitude
            current_altitude += g

            # Update maximum altitude if needed
            if current_altitude > max_altitude:
                max_altitude = current_altitude

        # Return the highest altitude
        return max_altitude