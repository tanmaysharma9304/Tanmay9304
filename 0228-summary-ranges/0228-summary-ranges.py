class Solution:
    def summaryRanges(self, nums):
        ans = []

        if not nums:
            return ans

        start = 0

        for i in range(len(nums) - 1):

            if nums[i + 1] != nums[i] + 1:

                if start == i:
                    ans.append(str(nums[i]))
                else:
                    ans.append(str(nums[start]) + "->" + str(nums[i]))

                start = i + 1

        if start == len(nums) - 1:
            ans.append(str(nums[start]))
        else:
            ans.append(str(nums[start]) + "->" + str(nums[-1]))

        return ans