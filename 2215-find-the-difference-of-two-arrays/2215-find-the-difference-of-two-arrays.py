class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert both arrays to sets (removes duplicates)
        set1 = set(nums1)
        set2 = set(nums2)

        # List to store elements in nums1 but not in nums2
        only_in_1 = []

        # Check elements of set1
        for num in set1:
            if num not in set2:
                only_in_1.append(num)

        # List to store elements in nums2 but not in nums1
        only_in_2 = []

        # Check elements of set2
        for num in set2:
            if num not in set1:
                only_in_2.append(num)

        # Return result
        return [only_in_1, only_in_2]