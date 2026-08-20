class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        seen = {}
        common = []

        for num in nums1:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1

        for num in nums2:
            if num in seen and seen[num] > 0:
                common.append(num)
                seen[num] -= 1

        return common