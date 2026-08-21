class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        seen = {}
        missing = []

        for num in nums:
            seen[num] = 1

        for i in range(1, len(nums) + 1):
            if i not in seen:
                missing.append(i)

        return missing