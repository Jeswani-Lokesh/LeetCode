class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Step 1: Count occurrences using dictionary
        count_map = {}

        for num in arr:
            # If num already in dictionary, increase count
            if num in count_map:
                count_map[num] += 1
            else:
                # Otherwise, initialize count as 1
                count_map[num] = 1

        # Step 2: Get all occurrence counts
        counts = list(count_map.values())

        # Step 3: Convert to set (removes duplicates)
        unique_counts = set(counts)

        # Step 4: Compare lengths
        # If lengths are same → all counts are unique
        return len(counts) == len(unique_counts)