class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort balloons by their ending position
        points.sort(key=lambda x: x[1])

        # We need at least one arrow for the first balloon
        arrows = 1

        # Shoot first arrow at the end of first balloon
        arrow_position = points[0][1]

        # Check remaining balloons
        for i in range(1, len(points)):
            # Current balloon start
            start = points[i][0]

            # Current balloon end
            end = points[i][1]

            # If current balloon starts after arrow position,
            # previous arrow cannot burst it
            if start > arrow_position:
                # Need one more arrow
                arrows += 1

                # Shoot new arrow at current balloon's end
                arrow_position = end

        # Return minimum arrows needed
        return arrows
        