class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        # Stack stores surviving asteroids
        stack = []

        # Process each asteroid
        for asteroid in asteroids:

            # Assume asteroid survives initially
            alive = True

            # Collision happens only if:
            # top of stack moves right (+)
            # current asteroid moves left (-)
            while alive and stack and stack[-1] > 0 and asteroid < 0:

                # If top asteroid is smaller
                if stack[-1] < abs(asteroid):

                    # Top asteroid explodes
                    stack.pop()

                    # Continue checking collisions
                    continue

                # If both are equal size
                elif stack[-1] == abs(asteroid):

                    # Both explode
                    stack.pop()

                # Current asteroid explodes
                alive = False

            # If asteroid survives all collisions
            if alive:
                stack.append(asteroid)

        # Return remaining asteroids
        return stack