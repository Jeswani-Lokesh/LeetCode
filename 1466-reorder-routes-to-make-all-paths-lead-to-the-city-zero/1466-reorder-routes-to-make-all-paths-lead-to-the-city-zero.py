class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Create graph for all cities
        graph = [[] for _ in range(n)]

        # Build graph
        for a, b in connections:
            # Original road is a -> b
            # If we travel from a to b, this road points away from city 0
            # So it needs reversal
            graph[a].append((b, 1))

            # Reverse direction b -> a is already useful toward city 0
            # So no reversal needed
            graph[b].append((a, 0))

        # Set to track visited cities
        visited = set()

        # DFS function
        def dfs(city):
            # Mark current city as visited
            visited.add(city)

            # Count reversals needed from this city
            changes = 0

            # Check all connected cities
            for neighbor, cost in graph[city]:
                # If neighbor not visited yet
                if neighbor not in visited:
                    # Add cost if road needs reversal
                    changes += cost

                    # Continue DFS
                    changes += dfs(neighbor)

            # Return total changes from this path
            return changes

        # Start from city 0
        return dfs(0)
        