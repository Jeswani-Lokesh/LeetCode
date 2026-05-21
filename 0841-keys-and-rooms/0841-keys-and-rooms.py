class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Set to store rooms we have visited
        visited = set()

        # Helper function to visit rooms
        def dfs(room):
            # If this room is already visited, stop
            if room in visited:
                return

            # Mark this room as visited
            visited.add(room)

            # Go through every key inside this room
            for key in rooms[room]:
                # Use the key to visit another room
                dfs(key)

        # Start from room 0
        dfs(0)

        # If visited rooms count equals total rooms, return True
        return len(visited) == len(rooms)