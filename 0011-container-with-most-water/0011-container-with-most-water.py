class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        # Move pointers until they meet
        while left < right:
            # Height is limited by the shorter line
            current_height = min(height[left], height[right])
            # Width between the two lines
            current_width = right - left
            # Compute area
            area = current_height * current_width
            # Update maximum area
            max_area = max(max_area, area)

            # Move the pointer at the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area