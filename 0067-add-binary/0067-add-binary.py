class Solution(object):
    def addBinary(self, a, b):

        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        ans = ""

        while i >= 0 or j >= 0 or carry:

            total = carry

            if i >= 0:
                total += int(a[i])

            if j >= 0:
                total += int(b[j])

            if total == 0:
                ans += "0"
                carry = 0

            elif total == 1:
                ans += "1"
                carry = 0

            elif total == 2:
                ans += "0"
                carry = 1

            elif total == 3:
                ans += "1"
                carry = 1

            i -= 1
            j -= 1

        return ans[::-1]