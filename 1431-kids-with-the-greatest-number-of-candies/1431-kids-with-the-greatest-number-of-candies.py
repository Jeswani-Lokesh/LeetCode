class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies among all kids
        max_candies = max(candies)

        # List to store result
        result = []

        # Check each kid
        for candy in candies:
            # If giving extra candies makes this kid have max or more
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        # Return the result list
        return result
        