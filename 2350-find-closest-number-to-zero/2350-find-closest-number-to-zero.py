class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for x in nums:
            if abs(x) < abs(closest):
                closest = x   # x is the  new abs-value of input elements

        if closest < 0 and abs(closest) in nums: # here we make sure the number is positive
            return abs(closest) # if negative persists, return the positive
        return closest
            

            # Time -> O(n)
            # Space -> O(1)


        