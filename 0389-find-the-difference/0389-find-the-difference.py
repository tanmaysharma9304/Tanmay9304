class Solution(object):
    def findTheDifference(self, s, t):
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count or count[char] == 0:
                return char
            count[char] -= 1