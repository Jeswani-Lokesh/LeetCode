class RecentCounter:

    def __init__(self):
        # Queue to store request times
        self.queue = deque()


    def ping(self, t: int) -> int:
        # Add current request time
        self.queue.append(t)

        # Remove old requests
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        # Remaining queue size is answer
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)