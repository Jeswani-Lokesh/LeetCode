class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Create an adjacency list for the graph
        # graph[a] = list of courses that depend on course a
        graph = [[] for _ in range(numCourses)]

        # Step 2: Create an indegree array
        # indegree[i] = number of prerequisites needed for course i
        indegree = [0] * numCourses

        # Step 3: Fill the graph and indegree array
        for course, prereq in prerequisites:
            # Add course as a neighbor of prereq
            graph[prereq].append(course)

            # Increase indegree of the course
            indegree[course] += 1

        # Step 4: Create a queue for courses with no prerequisites
        queue = deque()

        # Step 5: Add all courses with indegree 0 to the queue
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Step 6: Count how many courses we can complete
        completed_courses = 0

        # Step 7: Process courses in BFS order
        while queue:
            # Take a course that has no remaining prerequisites
            current = queue.popleft()

            # We can complete this course
            completed_courses += 1

            # Reduce indegree of dependent courses
            for neighbor in graph[current]:
                indegree[neighbor] -= 1

                # If a course now has no prerequisites, add it to the queue
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 8: If we completed all courses, return True
        return completed_courses == numCourses
        