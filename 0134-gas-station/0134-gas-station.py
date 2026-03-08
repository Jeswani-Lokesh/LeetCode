class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Total gas available across all stations
        total_gas = 0
        
        # Total cost required to travel all stations
        total_cost = 0
        
        # Current gas in tank while traveling
        tank = 0
        
        # Possible starting station
        start = 0

        # Loop through every gas station
        for i in range(len(gas)):
            
            # Add gas and cost to totals
            total_gas += gas[i]
            total_cost += cost[i]

            # Update current tank after leaving station i
            tank += gas[i] - cost[i]

            # If tank becomes negative
            if tank < 0:
                # This starting station cannot work
                # Move starting station to the next one
                start = i + 1

                # Reset tank
                tank = 0

        # If total gas is less than total cost, return -1
        if total_gas < total_cost:
            return -1

        # Otherwise return the valid starting station
        return start
        