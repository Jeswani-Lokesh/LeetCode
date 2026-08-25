class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start, current):
            # Every node in the tree is a valid subset — record it
            result.append(current[:])
            
            # Try adding each remaining element (only those after `start`)
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)   # i+1: never reuse earlier elements
                current.pop()               # backtrack
        
        backtrack(0, [])
        return result