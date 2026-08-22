class Solution:
    def maxSubsequence(self, nums, k):

        arr = []

        # value + original index
        for i in range(len(nums)):
            arr.append((nums[i], i))

        # values ko ascending order mein sort karo
        arr.sort()

        # reverse karke largest values pehle
        arr = arr[::-1]

        # top k elements
        selected = arr[:k]

        # selected ko original index ke according sort karo
        for i in range(len(selected)):
            for j in range(i + 1, len(selected)):

                if selected[i][1] > selected[j][1]:
                    temp = selected[i]
                    selected[i] = selected[j]
                    selected[j] = temp

        # sirf values answer mein
        ans = []

        for value, index in selected:
            ans.append(value)

        return ans