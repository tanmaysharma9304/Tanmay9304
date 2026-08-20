class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        big1 = None
        big2 = None
        big3 = None

        for num in nums:
            if num == big1 or num == big2 or num == big3:
                continue

            if big1 is None or num > big1:
                big3 = big2
                big2 = big1
                big1 = num

            elif big2 is None or num > big2:
                big3 = big2
                big2 = num

            elif big3 is None or num > big3:
                big3 = num
        if big3 is None:
            return big1

        return big3