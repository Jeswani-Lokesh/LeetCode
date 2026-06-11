class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Number of days
        n = len(temperatures)

        # Final answer
        result = [0] * n

        # Stack stores indices
        stack = []

        # Process each day
        for current_day in range(n):

            # Current temperature
            current_temp = temperatures[current_day]

            # While current temperature is warmer
            while stack and current_temp > temperatures[stack[-1]]:

                # Previous colder day
                previous_day = stack.pop()

                # Days waited
                result[previous_day] = current_day - previous_day

            # Store current day
            stack.append(current_day)

        return result