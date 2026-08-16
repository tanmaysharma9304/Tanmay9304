class Solution:
    def majorityElement(self, nums):
        
        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] = freq[nums[i]] + 1
        max_freq = 0
        answer = 0

        for num in freq:
            if freq[num] > max_freq:
                max_freq = freq[num]
                answer = num

        return answer