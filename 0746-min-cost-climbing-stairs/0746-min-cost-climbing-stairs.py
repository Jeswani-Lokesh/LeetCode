class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Cost to reach stair 0
        first = cost[0]

        # Cost to reach stair 1
        second = cost[1]

        # Compute minimum cost for remaining stairs
        for i in range(2, len(cost)):

            # Minimum cost to reach current stair
            current = cost[i] + min(first, second)

            # Move DP window forward
            first = second
            second = current

        # Can finish from last stair or second last stair
        return min(first, second)
        