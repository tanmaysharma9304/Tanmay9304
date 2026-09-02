class Solution(object):
    def checkZeroOnes(self, s):
        count_1 = 0
        count_0 = 0

        max_count_1 = 0
        max_count_0 = 0

        for i in range(len(s)):

            if s[i] == '1':
                count_1 += 1
                count_0 = 0

                if count_1 > max_count_1:
                    max_count_1 = count_1

            else:
                count_0 += 1
                count_1 = 0

                if count_0 > max_count_0:
                    max_count_0 = count_0

        if max_count_1 > max_count_0:
            return True
        else:
            return False