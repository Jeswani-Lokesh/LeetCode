class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Store all valid combinations
        result = []

        # Backtracking function
        def backtrack(start, current, remaining):

            # Valid combination found
            if remaining == 0:
                result.append(current[:])
                return

            # Try every candidate starting from 'start'
            for i in range(start, len(candidates)):

                # Skip if candidate exceeds remaining target
                if candidates[i] > remaining:
                    continue

                # Choose current candidate
                current.append(candidates[i])

                # Stay at i because the same number can be reused
                backtrack(
                    i,
                    current,
                    remaining - candidates[i]
                )

                # Undo the choice
                current.pop()

        backtrack(0, [], target)

        return result
        