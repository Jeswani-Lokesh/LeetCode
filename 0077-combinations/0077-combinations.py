class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        
        def backtrack(start, current):
            # Base case: we've chosen k numbers → a complete combination
            if len(current) == k:
                result.append(current[:])      # append a COPY
                return
            
            # Try each candidate from `start` to n
            for num in range(start, n + 1):
                current.append(num)            # choose
                backtrack(num + 1, current)    # recurse: next starts AFTER num
                current.pop()                  # un-choose (backtrack)
        
        backtrack(1, [])
        return result
        