class Solution:
    def tribonacci(self, n: int) -> int:
       # Base cases
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        # T0, T1, T2
        a = 0
        b = 1
        c = 1

        # Build sequence from T3 to Tn
        for i in range(3, n + 1):

            # Current tribonacci number
            current = a + b + c

            # Shift values forward
            a = b
            b = c
            c = current

        # c stores Tn
        return c