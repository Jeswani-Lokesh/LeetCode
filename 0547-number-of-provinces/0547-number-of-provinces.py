class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Number of cities
        n = len(isConnected)

        # Set to track visited cities
        visited = set()

        # Count of provinces
        provinces = 0

        # DFS function to visit all connected cities
        def dfs(city):
            # Mark current city as visited
            visited.add(city)

            # Check all other cities
            for other_city in range(n):
                # If connected and not visited
                if isConnected[city][other_city] == 1 and other_city not in visited:
                    # Visit that connected city
                    dfs(other_city)

        # Try starting DFS from every city
        for city in range(n):
            # If city has not been visited yet
            if city not in visited:
                # This starts a new province
                provinces += 1

                # Visit all cities in this province
                dfs(city)

        # Return total number of provinces
        return provinces