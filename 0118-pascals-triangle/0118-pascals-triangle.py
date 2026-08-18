class Solution(object):
    def generate(self, numRows):
        result = []

        if numRows == 0:
            return result

        result.append([1])

        for i in range(1, numRows):
            previous = result[-1]

            new = [1]

            for j in range(len(previous) - 1):
                new.append(previous[j] + previous[j + 1])

            new.append(1)

            result.append(new)

        return result