class Solution(object):
    def getRow(self, rowIndex):
        row = [1]

        for i in range(rowIndex):
            new = [1]

            for j in range(len(row) - 1):
                new.append(row[j] + row[j + 1])

            new.append(1)
            row = new

        return row