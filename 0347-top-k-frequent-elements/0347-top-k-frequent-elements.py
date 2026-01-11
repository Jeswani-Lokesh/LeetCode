class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        freq_map = Counter(nums)

        # Step 2: Use a min-heap to keep top k elements
        # Heap elements are (frequency, number)
        heap = []

        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))  # push frequency first
            if len(heap) > k:
                heapq.heappop(heap)  # remove lowest frequency

        # Step 3: Extract elements from heap
        return [num for freq, num in heap]
        