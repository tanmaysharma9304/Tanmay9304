class Solution(object):
    def longestCommonPrefix(self, strs):

        result = ""

        for i in range(len(strs[0])):

            ch = strs[0][i]

            for word in strs:

                if i >= len(word):
                    return result

                if word[i] != ch:
                    return result

            result = result + ch

        return result