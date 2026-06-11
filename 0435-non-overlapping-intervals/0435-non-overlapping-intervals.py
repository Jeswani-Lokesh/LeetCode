class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])

        # Count how many intervals we remove
        removals = 0

        # End time of the last interval we decided to keep
        previous_end = intervals[0][1]

        # Start checking from the second interval
        for i in range(1, len(intervals)):
            # Current interval start
            current_start = intervals[i][0]

            # Current interval end
            current_end = intervals[i][1]

            # If current interval overlaps with previous kept interval
            if current_start < previous_end:
                # Remove current interval
                removals += 1

            # If current interval does not overlap
            else:
                # Keep current interval
                previous_end = current_end

        # Return minimum removals
        return removals
        