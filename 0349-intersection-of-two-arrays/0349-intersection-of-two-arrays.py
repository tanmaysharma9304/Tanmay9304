class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        seen = {}

        for num in nums1:
            seen[num] = 1

        common = []

        for num in nums2:
            if num in seen and num not in common:
                common.append(num)

        return common