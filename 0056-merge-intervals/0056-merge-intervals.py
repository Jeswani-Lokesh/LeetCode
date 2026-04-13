class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # If there are no intervals, return an empty list
        if not intervals:
            return []

        # Sort intervals by their start value
        intervals.sort(key=lambda x: x[0])

        # Start the result with the first interval
        merged = [intervals[0]]

        # Go through the remaining intervals
        for i in range(1, len(intervals)):
            # Get the current interval
            current = intervals[i]

            # Get the last interval already added to merged
            last = merged[-1]

            # If current interval overlaps with the last interval
            if current[0] <= last[1]:
                # Merge them by updating the end value
                last[1] = max(last[1], current[1])
            else:
                # If they do not overlap, add current interval to result
                merged.append(current)

        # Return the merged intervals
        return merged
        