class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m

        while True:
            i = (left + right) // 2  # Partition in nums1
            j = half - i             # Complement partition in nums2

            # Edges of left and right halves
            Aleft = nums1[i - 1] if i > 0 else float('-inf')
            Aright = nums1[i] if i < m else float('inf')
            Bleft = nums2[j - 1] if j > 0 else float('-inf')
            Bright = nums2[j] if j < n else float('inf')

            # Valid partition
            if Aleft <= Bright and Bleft <= Aright:
                # Even total
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                # Odd total
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                right = i - 1  # Move left
            else:
                left = i + 1   # Move right
        