class Solution(object):
    def dominantIndex(self, nums):
        largest = max(nums)
        index = nums.index(largest)

        for i in range(len(nums)):
            if nums[i] != largest:
                if largest < 2 * nums[i]:
                    return -1

        return index