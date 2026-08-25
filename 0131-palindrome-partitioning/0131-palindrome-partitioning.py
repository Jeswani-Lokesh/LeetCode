class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, current):
            # Base case: consumed the whole string → valid partition
            if start == len(s):
                result.append(current[:])
                return
            
            # Try every possible next cut, from `start` to each `end`
            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                if is_palindrome(prefix):
                    current.append(prefix)          # choose
                    backtrack(end, current)         # recurse on the rest
                    current.pop()                   # un-choose
        
        backtrack(0, [])
        return result
        