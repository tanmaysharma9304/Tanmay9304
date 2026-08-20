class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minimum = nums[0]
        maximum = nums[0]

        for num in nums:
            if num < minimum:
                minimum = num

            if num > maximum:
                maximum = num

        for num in nums:
            if num != minimum and num != maximum:
                return num

        return -1