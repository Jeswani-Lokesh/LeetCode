class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Total number of workers
        n = len(costs)

        # Left heap for first candidates workers
        left_heap = []

        # Right heap for last candidates workers
        right_heap = []

        # Pointer for next worker from the left side
        left = 0

        # Pointer for next worker from the right side
        right = n - 1

        # Add initial left-side candidates
        while left <= right and len(left_heap) < candidates:
            # Push cost and index into left heap
            heapq.heappush(left_heap, (costs[left], left))

            # Move left pointer forward
            left += 1

        # Add initial right-side candidates
        while left <= right and len(right_heap) < candidates:
            # Push cost and index into right heap
            heapq.heappush(right_heap, (costs[right], right))

            # Move right pointer backward
            right -= 1

        # Store total hiring cost
        total_cost = 0

        # Hire exactly k workers
        for _ in range(k):
            # If right heap is empty, choose from left heap
            if not right_heap:
                cost, index = heapq.heappop(left_heap)

                # Add hired worker cost
                total_cost += cost

                # Refill left heap if workers remain
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1

            # If left heap is empty, choose from right heap
            elif not left_heap:
                cost, index = heapq.heappop(right_heap)

                # Add hired worker cost
                total_cost += cost

                # Refill right heap if workers remain
                if left <= right:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1

            # If left heap has smaller or equal worker
            elif left_heap[0] <= right_heap[0]:
                cost, index = heapq.heappop(left_heap)

                # Add hired worker cost
                total_cost += cost

                # Refill left heap
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1

            # Otherwise choose from right heap
            else:
                cost, index = heapq.heappop(right_heap)

                # Add hired worker cost
                total_cost += cost

                # Refill right heap
                if left <= right:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1

        # Return final total cost
        return total_cost
        