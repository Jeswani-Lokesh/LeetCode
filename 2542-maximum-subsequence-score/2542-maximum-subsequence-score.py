class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Pair each nums2 value with its nums1 value
        pairs = []

        # Build pairs like (nums2 value, nums1 value)
        for i in range(len(nums1)):
            pairs.append((nums2[i], nums1[i]))

        # Sort pairs by nums2 in decreasing order
        pairs.sort(reverse=True)

        # Min heap to store selected nums1 values
        heap = []

        # Running sum of nums1 values inside heap
        current_sum = 0

        # Best score found so far
        best_score = 0

        # Go through pairs from largest nums2 to smallest nums2
        for value2, value1 in pairs:
            # Add current nums1 value to heap
            heapq.heappush(heap, value1)

            # Add current nums1 value to running sum
            current_sum += value1

            # If heap has more than k elements
            if len(heap) > k:
                # Remove smallest nums1 value
                removed = heapq.heappop(heap)

                # Remove it from running sum
                current_sum -= removed

            # If we have exactly k selected values
            if len(heap) == k:
                # Since pairs are sorted by nums2 descending,
                # current value2 is the minimum nums2 among selected candidates
                score = current_sum * value2

                # Update best score
                best_score = max(best_score, score)

        # Return maximum score
        return best_score
        