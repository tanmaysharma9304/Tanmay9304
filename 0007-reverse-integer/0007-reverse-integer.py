class Solution(object):
    def reverse(self, x):

        if x < 0:
            x = str(x)
            x = x[1:]

            rev = ""

            for i in range(len(x) - 1, -1, -1):
                rev = rev + x[i]

            rev = "-" + rev

        else:
            x = str(x)

            rev = ""

            for i in range(len(x) - 1, -1, -1):
                rev = rev + x[i]

        result = int(rev)

        if result < -2147483648 or result > 2147483647:
            return 0

        return result