class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(current, remaining):
            # Base case: no more numbers to place → a complete permutation
            if not remaining:
                result.append(current[:])   # append a COPY
                return
            
            for i in range(len(remaining)):
                # Choose nums[i], recurse on the rest
                current.append(remaining[i])
                backtrack(current, remaining[:i] + remaining[i+1:])
                current.pop()   # undo the choice (backtrack)
        
        backtrack([], nums)
        return result