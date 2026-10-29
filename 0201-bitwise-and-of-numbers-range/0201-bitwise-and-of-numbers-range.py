class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Strip low bits until the two numbers share the same prefix
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        # Restore the prefix to its original position, zeros below
        return left << shift
        