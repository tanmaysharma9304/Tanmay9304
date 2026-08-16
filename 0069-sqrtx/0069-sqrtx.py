class Solution:
    def mySqrt(self, x):
        i = 1

        while i * i <= x:
            i = i + 1

        return i - 1