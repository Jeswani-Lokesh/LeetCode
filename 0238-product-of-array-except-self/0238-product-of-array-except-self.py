class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the size of the array
        n = len(nums)

        # Create the result array and fill it with 1
        result = [1] * n

        # This variable will store the product of elements to the left
        left_product = 1

        # First pass: store left products in result
        for i in range(n):
            # Put the current left product into result[i]
            result[i] = left_product

            # Update left product by multiplying with nums[i]
            left_product = left_product * nums[i]

        # This variable will store the product of elements to the right
        right_product = 1

        # Second pass: multiply right products into result
        for i in range(n - 1, -1, -1):
            # Multiply the current right product with result[i]
            result[i] = result[i] * right_product

            # Update right product by multiplying with nums[i]
            right_product = right_product * nums[i]

        # Return the final result array
        return result
        