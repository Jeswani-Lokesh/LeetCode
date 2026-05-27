class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create empty min heap
        heap = []

        # Process every number
        for num in nums:
            # Add number to heap
            heapq.heappush(heap, num)

            # If heap size becomes bigger than k
            if len(heap) > k:
                # Remove smallest element
                heapq.heappop(heap)

        # Heap top is kth largest element
        return heap[0]
        