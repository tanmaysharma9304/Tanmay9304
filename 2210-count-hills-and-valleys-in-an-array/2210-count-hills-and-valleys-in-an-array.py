class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        new = []
        for num in nums:
            if len(new) == 0 or new[-1] != num:
                new.append(num)

        count = 0
        for i in range(1, len(new) - 1):

            if new[i] > new[i - 1] and new[i] > new[i + 1]:
                count += 1

            elif new[i] < new[i - 1] and new[i] < new[i + 1]:
                count += 1

        return count