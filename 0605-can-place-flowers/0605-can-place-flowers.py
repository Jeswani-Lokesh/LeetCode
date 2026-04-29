class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Loop through each position in the flowerbed
        for i in range(len(flowerbed)):

            # Check if current position is empty
            if flowerbed[i] == 0:

                # Check left position
                # If i == 0, it means no left neighbor (valid)
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)

                # Check right position
                # If i is last index, no right neighbor (valid)
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                # If both sides are empty, we can plant here
                if left_empty and right_empty:
                    # Plant the flower
                    flowerbed[i] = 1

                    # Decrease n
                    n -= 1

                    # If we have planted all flowers
                    if n == 0:
                        return True

        # If we exit loop and still have flowers to plant
        return n <= 0
        