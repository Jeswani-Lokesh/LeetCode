class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Left pointer at the beginning
        left = 0
        
        # Right pointer at the end
        right = len(numbers) - 1
        
        # Continue until pointers meet
        while left < right:
            
            # Calculate the current sum
            current_sum = numbers[left] + numbers[right]
            
            # If we found the target
            if current_sum == target:
                # Return 1-based indices
                return [left + 1, right + 1]
            
            # If sum is too small
            elif current_sum < target:
                # Move left pointer to increase sum
                left += 1
            
            # If sum is too large
            else:
                # Move right pointer to decrease sum
                right -= 1
        