class Solution:
    def removeDuplicates(self, nums):
        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[j - 1]:
                nums[j] = nums[i]
                j = j + 1

        return j