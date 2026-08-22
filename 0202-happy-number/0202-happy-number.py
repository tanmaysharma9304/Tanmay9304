class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        result = []

        while n != 1:

            if n in result:
                return False

            result.append(n)

            total = 0

            while n > 0:
                digit = n % 10
                total = total + digit * digit
                n = n // 10

            n = total

        return True