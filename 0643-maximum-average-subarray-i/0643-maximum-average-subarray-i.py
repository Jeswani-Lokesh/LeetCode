class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Step 1: Calculate sum of first window of size k
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]

        # This will store the maximum sum found
        max_sum = window_sum

        # Step 2: Slide the window
        for i in range(k, len(nums)):
            # Add next element to window
            window_sum += nums[i]

            # Remove element that is leaving the window
            window_sum -= nums[i - k]

            # Update max_sum if needed
            if window_sum > max_sum:
                max_sum = window_sum

        # Step 3: Return average
        return max_sum / k