class Solution(object):
    def reverseByType(self, s):
        letters = []
        special = []

        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                special.append(ch)

        result = []

        for ch in s:
            if ch.isalpha():
                result.append(letters.pop())
            else:
                result.append(special.pop())

        return ''.join(result)