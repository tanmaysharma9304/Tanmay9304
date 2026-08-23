class Solution:
    def maxSubsequence(self, nums, k):

        arr = []

        for i in range(len(nums)):
            arr.append((nums[i], i))

        arr.sort()
        arr = arr[::-1]

        top = arr[:k]

        ans = []

        for i in range(len(nums)):
            for value, index in top:
                if i == index:
                    ans.append(value)

                    if len(ans) == k:
                        return ans