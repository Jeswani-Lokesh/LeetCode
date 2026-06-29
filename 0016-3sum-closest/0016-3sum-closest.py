class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array
        nums.sort()

        # Initialize closest sum with first three numbers
        closest_sum = nums[0] + nums[1] + nums[2]

        # Fix first number
        for i in range(len(nums) - 2):

            # Left pointer
            left = i + 1

            # Right pointer
            right = len(nums) - 1

            # Search for best pair
            while left < right:

                # Current sum
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest sum if current is nearer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Exact match found
                if current_sum == target:
                    return target

                # Need a larger sum
                elif current_sum < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        # Return closest sum
        return closest_sum
        